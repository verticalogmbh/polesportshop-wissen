"""
PoleGrip TAC — Erstanlage (ERSTER Technik-Artikel, kein Kleidungsstück).

Single-SKU (keine Größen/Farben) -> keine Variationen, keine Klamotten-Merkmale.
Kategorie per ID (Zubehör 2 + Grip Produkte 11, E106) statt Name -> keine Duplikate.
Bild quadratisch (crop_profile 'tech' 1:1). EK £3,25 GBP (100 Stk, 75/100-Zoll-Logik
schon eingepreist), konservativer GBP-Kurs (constants.FX_KONSERVATIV), per-Lieferant
gld_aufschlag 2,00 € (echte Fracht/Zoll ~€1,40 + Puffer statt 5-€-Kleidungs-Pauschale)
-> VK 11,90 @40 % Marge. Markentext aus Mapping, Content aus polegrip_content.json.

Aufruf: python -m pipeline.build_polegrip [--no-image]
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path

from . import config, constants as C, spec, numbering, content as Cont
from .pricing import vk_aus_marge
from .csv._writer import write_csv, fmt_decimal
from .csv import bestellung

SUPPLIER_KEY = "POLEGRIP"
EK_GBP = 3.25
MENGE = 100
NAME = "PoleGrip TAC 50ml"
ARTNR_LIEF = "PG-PoleGrip-TAC"
CONTENT_KEY = "PG-PoleGrip-TAC"
BESTELL_REF = "Bestellung PG-2026-01 | Rechnung PoleAmorUK #4937 | PoleGrip TAC"
BILD_PATH = config.PIPELINE_DIR / ".incoming" / "polegrip_bottle.jpg"

STAMM_COLS = [
    "Artikelnummer", "Artikelnummer (Lieferant)", "HAN", "Artikelname", "Hersteller",
    "Steuerklasse", "TARIC-Code", "Kategorien",
    "EK Netto (für GLD)", "Brutto-VK", "Netto-EK",
    "Bestandsführung aktiv", "Neu im Sortiment", "Neu im Sortiment seit",
    "Artikelgewicht", "Versandgewicht", "Versandklasse", "Herkunftsland",
    "Ist Standardlieferant", "Lieferzeit in Tagen (Lieferant)",
    "Global-Englisch: Artikelname", "Global-Französisch: Artikelname",
    "Global-Italienisch: Artikelname", "Global-Spanisch: Artikelname",
    "Titel-Tag (SEO)", "Meta-Description (SEO)",
    "Global-Englisch: Titel-Tag", "Global-Englisch: Meta-Description",
    "Global-Französisch: Titel-Tag", "Global-Französisch: Meta-Description",
    "Global-Italienisch: Titel-Tag", "Global-Italienisch: Meta-Description",
    "Global-Spanisch: Titel-Tag", "Global-Spanisch: Meta-Description",
    "Bild 1", "Bild 2", "Bild 3", "EAN",
]
ATTR_COLS = ["Lieferant", "Artikelnummer (Lieferant)", "Attributname", "Attributwert",
             "Englisch: Attributwert", "Französisch: Attributwert",
             "Italienisch: Attributwert", "Spanisch: Attributwert"]
LANGPFX = {"en": "Englisch", "fr": "Französisch", "it": "Italienisch", "es": "Spanisch"}


def _next_artnr(persist: bool) -> str:
    st = numbering.load_state()
    n = st["artikel_next"]
    artnr = f'{st.get("praefix", "A")}{n}'
    if persist:
        st["artikel_next"] = n + 1
        numbering.STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    return artnr


def _bild_urls(with_image: bool, sup: dict) -> list[str]:
    if not with_image or not BILD_PATH.exists():
        return []
    from .images import process, r2
    imgs = process.process_vater([BILD_PATH.resolve().as_uri()], sup["crop_profile"])  # file:// -> tech-Crop 1:1
    client = r2.make_client()
    urls = r2.upload_vater(client, sup["r2_prefix"], ARTNR_LIEF, imgs)
    r2.build_originals_index(client, sup["r2_prefix"], {ARTNR_LIEF: NAME}, titel=f"{sup['marke_kurz']} Originalbilder")
    r2.build_master_index(client)
    return urls


def main(with_image: bool = True, persist: bool = True) -> dict:
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    run_date = datetime.now().strftime("%d.%m.%Y")
    sup = config.get_supplier(SUPPLIER_KEY)

    fx = C.FX_KONSERVATIV.get(sup["waehrung"], 1.0)
    ek_eur = round(EK_GBP * fx, 2)
    gld = round(ek_eur + float(sup["gld_aufschlag"]), 2)
    vk = vk_aus_marge(gld)
    artnr = _next_artnr(persist)
    bild = _bild_urls(with_image, sup)

    d = dict(spec.DEFAULTS)
    row = {c: "" for c in STAMM_COLS}
    row.update({
        "Artikelnummer": artnr, "Artikelnummer (Lieferant)": ARTNR_LIEF, "Artikelname": NAME,
        "Hersteller": sup["hersteller"], "Steuerklasse": sup["steuerklasse"],
        "TARIC-Code": str(sup["taric_code"]), "Kategorien": sup["kategorie_ids"],
        "EK Netto (für GLD)": fmt_decimal(gld), "Brutto-VK": fmt_decimal(vk),
        "Netto-EK": fmt_decimal(round(EK_GBP, 2)),  # Lieferanten-EK in Original-Währung GBP (E97)
        "Bestandsführung aktiv": "Y", "Neu im Sortiment": "Y", "Neu im Sortiment seit": run_date,
        "Artikelgewicht": str(sup["article_weight_kg"]).replace(".", ","),
        "Versandgewicht": str(sup["article_weight_kg"]).replace(".", ","),
        "Versandklasse": "standard", "Herkunftsland": sup["herkunftsland"],
        "Ist Standardlieferant": "Y", "Lieferzeit in Tagen (Lieferant)": "",
        "Global-Englisch: Artikelname": NAME, "Global-Französisch: Artikelname": NAME,
        "Global-Italienisch: Artikelname": NAME, "Global-Spanisch: Artikelname": NAME,
        "Titel-Tag (SEO)": spec.SEO_TITEL["de"].format(name=NAME),
        "Meta-Description (SEO)": spec.SEO_META["de"].format(name=NAME),
        "EAN": "",
    })
    for lang, pfx in [("en", "Global-Englisch"), ("fr", "Global-Französisch"),
                      ("it", "Global-Italienisch"), ("es", "Global-Spanisch")]:
        row[f"{pfx}: Titel-Tag"] = spec.SEO_TITEL[lang].format(name=NAME)
        row[f"{pfx}: Meta-Description"] = spec.SEO_META[lang].format(name=NAME)
    for i, u in enumerate(bild[:3], 1):
        row[f"Bild {i}"] = u

    # Attribute: markentext (Mapping) + artikeldetails/material_and_care/size_and_fit (Content)
    markentext = Cont.markentext_from_mapping(sup)
    content = json.loads((config.PIPELINE_DIR / "content" / "polegrip_content.json").read_text("utf-8"))
    attr = content[CONTENT_KEY]["attribute"]
    attr_rows = []

    def _attr(name, per_lang):
        r = {"Lieferant": sup["anzeigename"], "Artikelnummer (Lieferant)": ARTNR_LIEF,
             "Attributname": name, "Attributwert": per_lang["de"]}
        for lang, pfx in LANGPFX.items():
            r[f"{pfx}: Attributwert"] = per_lang[lang]
        attr_rows.append(r)

    _attr("markentext", markentext)
    for a in ["artikeldetails", "material_and_care", "size_and_fit"]:
        _attr(a, attr[a])

    # Lieferantenbestellung (1 Zeile, keine Größen)
    lz = int(sup.get("lieferzeit_tage", 0) or 0)
    lieferdatum = (datetime.now() + timedelta(days=lz)).strftime("%d.%m.%Y")
    be_rows = [{"Artikelnummer": artnr, "Menge": str(MENGE), "Lieferdatum": lieferdatum,
                "Zugehörige Auftragsnummer": BESTELL_REF, "Lieferant": sup["anzeigename"],
                "Warenlager": bestellung.WARENLAGER_DEFAULT, "Firma": bestellung.FIRMA_DEFAULT,
                "Benutzer": bestellung.BENUTZER_DEFAULT}]

    out = config.OUTPUTS_DIR / f"{sup['kuerzel']}_{stamp}"
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / f"1_Stammdaten_{sup['kuerzel']}_{stamp}.csv", STAMM_COLS, [row], quote_all=False)
    write_csv(out / f"4_Attribute_{sup['kuerzel']}_{stamp}.csv", ATTR_COLS, attr_rows, quote_all=True)
    write_csv(out / f"6_Lieferantenbestellung_{sup['kuerzel']}_{stamp}.csv", bestellung.COLUMNS, be_rows, quote_all=False)
    config.copy_to_downloads(out)
    return {"out": out, "artnr": artnr, "ek_eur": ek_eur, "gld": gld, "vk": vk, "bild": bild}


if __name__ == "__main__":
    import sys
    r = main(with_image="--no-image" not in sys.argv)
    print(f"PoleGrip {r['artnr']}: EK_eur {r['ek_eur']} -> GLD {r['gld']} -> VK {r['vk']} | Bild: {len(r['bild'])}")
    print(f"Out: {r['out']}")
