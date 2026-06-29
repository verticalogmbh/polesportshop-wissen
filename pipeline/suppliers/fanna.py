"""
Fanna — Erstanlage (Rechnung FANNA-2026-1329, Order #10908). Shopify-Fetch.

NUR die 2 neuen Styles aus Mercis Liste: Grace Top + Grace Bottom in SOFT GREEN.
Der Shop führt Grace auch in Black/Espresso und bis XXL — wir filtern auf SOFT GREEN
und voller Shop-Stand XS–XL (pures XXL raus). Barcodes: Shop-GTIN leer, nur SKU-Codes
(GRACETO…/GRACEBO…) -> ins HAN-Feld (barcode_feld=HAN im Mapping). Bottom als garment_type
'Bottom' -> generischer Outfit-Cross-Sell Top↔Bottom (gleiches Modell „Grace", Soft Green).
"""
from __future__ import annotations

import json
import urllib.request

from ..model import Vater, Kind

_UA = {"User-Agent": "Mozilla/5.0"}
ALLOWED_GROESSEN = ["XS", "S", "M", "L", "XL"]   # XXL raus
COLOR = "soft green"

# (handle, modell_basis, garment_type)
PRODUCTS = [
    ("grace-top",    "Grace", "Top"),
    ("grace-bottom", "Grace", "Bottom"),
]


def _fetch(handle: str) -> dict:
    req = urllib.request.Request(f"https://fannapolewear.com/products/{handle}.json", headers=_UA)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["product"]


def _is_soft_green(v: dict) -> bool:
    return any((v.get(k) or "").strip().lower() == COLOR for k in ("option1", "option2", "option3"))


def _size_of(v: dict) -> str | None:
    for k in ("option1", "option2", "option3"):
        val = (v.get(k) or "").strip()
        if val.upper() in ALLOWED_GROESSEN:
            return val.upper()
    return None


def build_vaeter() -> list[Vater]:
    vaeter = []
    for handle, modell, typ in PRODUCTS:
        p = _fetch(handle)
        sg_variants = [v for v in p.get("variants", []) if _is_soft_green(v)]
        # Kinder: nur erlaubte Größen, in Größen-Reihenfolge; SKU -> ean (landet via HAN)
        by_size = {}
        for v in sg_variants:
            s = _size_of(v)
            if s and s not in by_size:
                by_size[s] = v.get("sku") or ""
        kinder = [Kind(groesse=g, groesse_raw=g, position=i, ean=by_size[g])
                  for i, g in enumerate(s for s in ALLOWED_GROESSEN if s in by_size)]
        # Bilder: Fanna taggt Bilder nicht per variant_id, sondern über den Dateinamen
        # (…soft-green…/…black…/…espresso…). Strategie: das dedizierte Soft-Green-Bild als
        # Hero zuerst, dann die generischen Lifestyle/Gruppen-Shots (ohne Farb-Token);
        # die farb-spezifischen Black/Espresso-Bilder fliegen raus.
        def _img_color(src: str):
            s = src.lower()
            for c in ("soft-green", "black", "espresso"):
                if c in s:
                    return c
            return None
        imgs = [i for i in p.get("images", []) if i.get("src")]
        sg_named = sorted((i for i in imgs if _img_color(i["src"]) == "soft-green"),
                          key=lambda i: i.get("position", 0))
        generic = sorted((i for i in imgs if _img_color(i["src"]) is None),
                         key=lambda i: i.get("position", 0))
        images = [i["src"] for i in (sg_named + generic)][:10]
        vaeter.append(Vater(
            handle=handle, product_id=p.get("id", 0), title_raw=p.get("title", ""),
            vendor="Fanna", modell_basis=modell, garment_type=typ, farbe_raw=COLOR,
            body_html=p.get("body_html", ""), image_urls=images, kinder=kinder,
        ))
    return vaeter
