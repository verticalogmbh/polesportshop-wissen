"""
Shark Polewear — Erstanlage (Bestellung BE20261014488, Rechnung #14 vom 24.06.2026). Shopify-Fetch.

NUR die 12 NEUEN Artikel aus Dens Link-Liste (Serenity/Capri/Charlotte/Aura in Wine/Grape/
Sapphira) — die übrigen Rechnungspositionen sind Bestandsartikel und gehören NICHT hierher.
Größen = voller Shop-Stand XS–XL (XXL raus). EK in USD (Rechnung), Barcodes je Größe aus dem Shop.
"""
from __future__ import annotations

import json
import urllib.request

from ..model import Vater, Kind

_UA = {"User-Agent": "Mozilla/5.0"}
ALLOWED_GROESSEN = ["XS", "S", "M", "L", "XL"]

# (handle, modell_basis, garment_type, farbe_raw)
PRODUCTS = [
    ("serenity-top-wine",        "Serenity",  "Top",    "wine"),
    ("serenity-shorts-wine",     "Serenity",  "Shorts", "wine"),
    ("serenity-top-grape",       "Serenity",  "Top",    "grape"),
    ("serenity-shorts-grape",    "Serenity",  "Shorts", "grape"),
    ("serenity-top-sapphira",    "Serenity",  "Top",    "sapphira"),
    ("serenity-shorts-sapphira", "Serenity",  "Shorts", "sapphira"),
    ("charlotte-shorts-grape",   "Charlotte", "Shorts", "grape"),
    ("aura-top-grape",           "Aura",      "Top",    "grape"),
    ("capri-top-wine",           "Capri",     "Top",    "wine"),
    ("capri-shorts-wine",        "Capri",     "Shorts", "wine"),
    ("capri-top-sapphira",       "Capri",     "Top",    "sapphira"),
    ("capri-shorts-sapphira",    "Capri",     "Shorts", "sapphira"),
]


def _fetch(handle: str) -> dict:
    req = urllib.request.Request(f"https://sharkpolewear.com/products/{handle}.json", headers=_UA)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["product"]


def build_vaeter() -> list[Vater]:
    vaeter = []
    for handle, modell, typ, farbe in PRODUCTS:
        p = _fetch(handle)
        images = [i["src"] for i in p.get("images", []) if i.get("src")]
        shop_sizes = {v.get("title") for v in p.get("variants", [])}
        groessen = [g for g in ALLOWED_GROESSEN if g in shop_sizes]  # voller Shop-Stand, XXL raus
        kinder = [Kind(groesse=g, groesse_raw=g, position=i) for i, g in enumerate(groessen)]
        vaeter.append(Vater(
            handle=handle, product_id=p.get("id", 0), title_raw=p.get("title", ""),
            vendor="Sharkpolewear", modell_basis=modell, garment_type=typ, farbe_raw=farbe,
            body_html=p.get("body_html", ""), image_urls=images, kinder=kinder,
        ))
    return vaeter
