"""
Lunalae — Odessa-Lieferung (Rechnung #D413, 2026-06-17). Shopify-Fetch.

6 Väter: Odessa Mesh Zip Top + Odessa Mesh High Waist Bottoms, je Black/Chocolate/White.
Top->Top, Bottoms->Bottom (Cross-Selling Top<->Bottom). AU6-14 -> XS-XL.
Teilt Fetch/AU-Mapping mit suppliers.lunalae.
"""
from __future__ import annotations

from ..model import Vater, Kind
from .lunalae import _fetch, AU_MAP

# handle, modell_basis, garment_type, farbe_raw
PRODUCTS = [
    ("odessa-mesh-zip-top-black", "Odessa", "Top", "black"),
    ("odessa-mesh-zip-top-chocolate", "Odessa", "Top", "chocolate"),
    ("odessa-mesh-zip-top-white", "Odessa", "Top", "white"),
    ("odessa-mesh-high-waist-bottoms-black", "Odessa", "Bottom", "black"),
    ("odessa-mesh-high-waist-bottoms-chocolate", "Odessa", "Bottom", "chocolate"),
    ("odessa-mesh-high-waist-bottoms-white", "Odessa", "Bottom", "white"),
]


def build_vaeter() -> list[Vater]:
    import re
    vaeter = []
    for handle, modell, typ, farbe in PRODUCTS:
        p = _fetch(handle)
        seen, kinder = set(), []
        for v in p["variants"]:
            sval = v.get("option2") or v.get("option1") or ""
            m = re.search(r"AU\s*(\d+)", sval)
            if not m:
                continue
            letter = AU_MAP.get(m.group(1))
            if letter and letter not in seen:
                seen.add(letter)
                kinder.append(Kind(groesse=letter, groesse_raw=sval, position=len(kinder)))
        images = [img["src"] for img in p.get("images", []) if img.get("src")]
        vaeter.append(Vater(
            handle=handle, product_id=p.get("id", 0), title_raw=p["title"],
            vendor="Lunalae", modell_basis=modell, garment_type=typ, farbe_raw=farbe,
            body_html=p.get("body_html", ""), image_urls=images, kinder=kinder,
        ))
    return vaeter
