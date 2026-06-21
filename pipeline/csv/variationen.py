"""
CSV 2: Variationen (12 Spalten, run_brief §5).
Eine Zeile pro Größen-Variante des Vaters. Darstellungsform IMGSWATCHES
(= JTL-UI-Option „Swatches", E101). ACHTUNG Mapping: Import-Wert IMGSWATCHES → UI „Swatches";
TEXTSWATCHES → UI „Textbox" (NICHT was wir wollen); SELECTBOX → „Dropdown"; RADIO → „Radiobutton".
JTL-Hinweis: greift per Ameise manchmal erst nach einmaligem manuellem Umschalten in WaWi.
Variationsname lokalisiert (Größe/Size/Taille/Taglia/Talla); Werte universal.
"""
from __future__ import annotations

from .. import spec, constants as C
from ..model import Vater


def _rank(groesse: str, position: int = 0) -> int:
    # Standardgrößen behalten ihren absoluten Rang (XS=0..XXL=5). Nicht-Standard-
    # Werte (z.B. kombinierte Cup-Größen „XS/S Fairy") sortieren stabil nach ihrer
    # Quell-Position, hinter den Standardgrößen.
    if groesse in C.GROESSEN_RANG:
        return C.GROESSEN_RANG.index(groesse)
    return len(C.GROESSEN_RANG) + position

COLUMNS = [
    "Artikelnummer", "Variationsname", "Darstellungsform", "Variationswertname",
    "Global-Englisch: Variationsname", "Global-Englisch: Variationswertname",
    "Global-Französisch: Variationsname", "Global-Französisch: Variationswertname",
    "Global-Italienisch: Variationsname", "Global-Italienisch: Variationswertname",
    "Global-Spanisch: Variationsname", "Global-Spanisch: Variationswertname",
    # JTL-Ameise sortiert Variationswerte sonst ALPHABETISCH (L,M,S,XS). Mit
    # expliziter Sortiernummer respektiert JTL die Reihenfolge (XS=1..XL=5).
    "Sortiernummer Variation", "Sortiernummer Variationswert",
]

VARIATIONSNAME = {"de": "Größe", "en": "Size", "fr": "Taille", "it": "Taglia", "es": "Talla"}


def build_rows(vaeter: list[Vater], supplier: dict, run_date: str) -> list[dict]:
    rows: list[dict] = []
    for v in vaeter:
        # Weg B (E94): Variation referenziert den Vater über dessen A-Nummer.
        # Aufsteigend ausgeben; die Anzeige-Reihenfolge steuert die Sortiernummer.
        for k in sorted(v.kinder, key=lambda x: _rank(x.groesse, x.position)):
            sort_wert = _rank(k.groesse, k.position) + 1  # XS=1..XL=5; kombinierte Werte dahinter
            rows.append({
                "Artikelnummer": v.artikelnummer,
                "Variationsname": VARIATIONSNAME["de"], "Darstellungsform": "IMGSWATCHES",
                "Variationswertname": k.groesse,
                "Global-Englisch: Variationsname": VARIATIONSNAME["en"],
                "Global-Englisch: Variationswertname": k.groesse,
                "Global-Französisch: Variationsname": VARIATIONSNAME["fr"],
                "Global-Französisch: Variationswertname": k.groesse,
                "Global-Italienisch: Variationsname": VARIATIONSNAME["it"],
                "Global-Italienisch: Variationswertname": k.groesse,
                "Global-Spanisch: Variationsname": VARIATIONSNAME["es"],
                "Global-Spanisch: Variationswertname": k.groesse,
                "Sortiernummer Variation": "1",
                "Sortiernummer Variationswert": str(sort_wert),
            })
    return rows
