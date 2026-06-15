"""
Rolling (VNDA-Plattform, Anti-Bot) — Väter-Builder aus Browser-Scrape (2026-06-15).

Die 4 Ceci-Botanica-Artikel wurden via Claude-in-Chrome gescraped (shoprolling.com.br
liefert 403 für urllib/WebFetch). Bra->Top, Panty->Bottom (Bottom->Shorts im DE-Namen
E76 + Kategorie Pole Dance Shorts + Cross-Selling Top<->Bottom). Größen fix XS-XL.
Bild-CDN cdn.vnda.com.br ist offen (Full-Res ladbar).
"""
from __future__ import annotations

from ..model import Vater, Kind
from .. import constants as C

FIXED_SIZES = ["XS", "S", "M", "L", "XL"]
_B = "https://cdn.vnda.com.br/shoprolling/2026/04/05/"

# (modell, garment_type, farbe_raw, [bild-dateinamen])
PRODUCTS = [
    ("Ceci", "Top", "black", [
        "22_42_10_133_rolling-20-1595-2-22044520.JPG",
        "22_42_09_596_rolling-20-1564-2-22044850.JPG",
        "22_42_10_551_rolling-20-1604-2-22046170.JPG",
        "22_42_14_125_rolling-20-1598-2-22044650.JPG",
        "22_42_09_573_rolling-20-1591-2-22044770.JPG"]),
    ("Ceci", "Bottom", "black", [
        "22_39_55_306_rolling-20-1606-2-22042450.JPG",
        "22_39_55_826_rolling-20-1564-2-22042560.JPG",
        "22_39_55_347_rolling-20-1594-2-202-22042440.JPG",
        "22_39_55_311_rolling-20-1604-2-22042270.JPG",
        "22_39_55_218_rolling-20-1591-2-202-22042450.JPG"]),
    ("Ceci", "Top", "white", [
        "22_38_14_678_img_8640-22045000.JPG",
        "22_38_14_807_rolling-20-1522-2-22046470.JPG",
        "22_38_14_960_rolling-20-1525-2-22048340.JPG"]),
    ("Ceci", "Bottom", "white", [
        "22_35_38_767_rolling-20-1501-2-22048070.JPG",
        "22_35_38_895_rolling-20-1525-2-22049940.JPG",
        "22_35_38_528_img_8640-22047860.JPG"]),
]


def build_vaeter() -> list[Vater]:
    vaeter = []
    for modell, typ, farbe, bilder in PRODUCTS:
        kinder = [Kind(groesse=s, groesse_raw=s, position=i)
                  for i, s in enumerate(FIXED_SIZES)]
        vaeter.append(Vater(
            handle="", product_id=0, title_raw=f"{modell} {typ} {farbe}",
            vendor="Rolling Clothing",
            modell_basis=modell, garment_type=typ, farbe_raw=farbe,
            image_urls=[_B + b for b in bilder], kinder=kinder,
        ))
    return vaeter
