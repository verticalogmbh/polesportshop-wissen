"""
Oksa Wear — Erstanlage (Packliste INV81.83, ORDER #81). Shopify-Fetch.

NUR die 17 neuen Artikel aus Dens Link-Liste (ORDER #81). Die Rechnung INV83
(BE20261013716) listet ANDERE Bestandsartikel — die gehören NICHT hierher. Jeder
Shop-Handle ist EINE Farbe (kein Color-Filter nötig). Größen XS–XL (Socken XS–L).
EK in USD (Packliste). Barcodes (8-stellig, nicht durchgängig valide GTIN) -> HAN.

Sonder-Typen (Tjorben 2026-06-29): Skirt Siena -> name_typ 'Rock' (Bottom-Filter);
Knee Socks -> garment_type 'Accessoire' (Kategorie Accessoires), name_typ 'Knee Socks',
leerer Modellname -> „Oksa Wear Kniestrümpfe Black". Bralette/Crop Top -> Top.
Alle Bottoms (Shorts + Skirt) als 'Bottom' -> Auto-Cross-Sell Top<->Bottom je Modell+Farbe.
"""
from __future__ import annotations

import json
import urllib.request

from ..model import Vater, Kind

_UA = {"User-Agent": "Mozilla/5.0"}
ALLOWED_GROESSEN = ["XS", "S", "M", "L", "XL"]

# (handle, modell_basis, garment_type, name_typ, farbe_raw)
PRODUCTS = [
    ("top-jersey-black",                       "Jersey", "Top",        None,         "black"),
    ("shorts-jadore-black-white-copy",         "Jersey", "Bottom",     None,         "black"),        # = Shorts Jersey Black
    ("top-jadore-black-white",                 "Jadore", "Top",        None,         "black-white"),
    ("shorts-jadore-black-white",              "Jadore", "Bottom",     None,         "black-white"),
    ("crop-top-siena-white",                   "Siena",  "Top",        None,         "white"),
    ("crop-top-siena-black",                   "Siena",  "Top",        None,         "black"),
    ("skirt-shorts-siena-black",               "Siena",  "Bottom",     "Rock",       "black"),
    ("skirt-shorts-siena-white",               "Siena",  "Bottom",     "Rock",       "white"),
    ("top-agatha-red",                         "Agatha", "Top",        None,         "red"),
    ("top-agatha-black",                       "Agatha", "Top",        None,         "black"),
    ("bralette-top-agatha-lilac",              "Agatha", "Top",        None,         "lilac"),
    ("shorts-agatha-red",                      "Agatha", "Bottom",     None,         "red"),
    ("shorts-agatha-black",                    "Agatha", "Bottom",     None,         "black"),
    ("high-waisted-shorts-agatha-lilac",       "Agatha", "Bottom",     None,         "lilac"),
    ("top-strict-light-pink",                  "Strict", "Top",        None,         "light pink"),
    ("high-waisted-shorts-strict-light-pink",  "Strict", "Bottom",     None,         "light pink"),
    ("knee-socks-oksa-black",                  "",       "Accessoire", "Knee Socks", "black"),
]


def _fetch(handle: str) -> dict:
    req = urllib.request.Request(f"https://oksawear.com/products/{handle}.json", headers=_UA)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["product"]


def _size_of(v: dict) -> str | None:
    for k in ("option1", "option2", "option3"):
        val = (v.get(k) or "").strip().upper()
        if val in ALLOWED_GROESSEN:
            return val
    return None


def build_vaeter() -> list[Vater]:
    vaeter = []
    for handle, modell, typ, name_typ, farbe in PRODUCTS:
        p = _fetch(handle)
        by_size = {}
        for v in p.get("variants", []):
            s = _size_of(v)
            if s and s not in by_size:
                by_size[s] = (v.get("barcode") or "").strip()   # -> HAN
        kinder = [Kind(groesse=g, groesse_raw=g, position=i, ean=by_size[g])
                  for i, g in enumerate(s for s in ALLOWED_GROESSEN if s in by_size)]
        images = [i["src"] for i in p.get("images", []) if i.get("src")][:10]
        vaeter.append(Vater(
            handle=handle, product_id=p.get("id", 0), title_raw=p.get("title", ""),
            vendor="Oksa Wear", modell_basis=modell, garment_type=typ,
            name_typ=name_typ, farbe_raw=farbe,
            body_html=p.get("body_html", ""), image_urls=images, kinder=kinder,
        ))
    return vaeter
