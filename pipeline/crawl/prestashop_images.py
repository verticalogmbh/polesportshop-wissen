"""
PrestaShop / Click-Shop Galerie-Bild-Extraktor — Original-Auflösung.

Standard-Weg, um Produktbilder von Hersteller-Shops auf der PrestaShop/Click-Shop-
Plattform zu ziehen (z.B. POLE ADDICT, shop.poleaddict.eu) — analog crawl/shopify_json
für Shopify. Liefert die Galerie-Originalbilder eines Produkts in DOM-Reihenfolge.

Mechanik: Galerie-Bilder tragen im HTML ein `data-image-announcement="<originaldatei>"`
und stehen bei einer `productGfx_<id>_<W>_<H>`-Cache-URL. Das Original liegt unter
`/userdata/public/gfx/<id>/<originaldatei>` (hochauflösend; der Cache ist nur 500x500
und damit zu klein für den 1000x1500-Crop).
"""
from __future__ import annotations

import re
import urllib.parse
import urllib.request

_UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=_UA)
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")


def _reachable(url: str) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD", headers=_UA)
        return urllib.request.urlopen(req, timeout=15).status == 200
    except Exception:
        return False


def gallery_originals(product_url: str, check: bool = True) -> list[dict]:
    """[{id, filename, url}] der Galerie-Originale in DOM-Reihenfolge.
    check=True wirft nicht-erreichbare (404) Originale raus."""
    parts = urllib.parse.urlsplit(product_url)
    base = f"{parts.scheme}://{parts.netloc}"
    html = _fetch(product_url)

    toks: list[tuple] = []
    for m in re.finditer(r'productGfx_(\d+)_\d+_\d+', html):
        toks.append((m.start(), "id", m.group(1)))
    for m in re.finditer(r'data-image-announcement="([^"]+)"', html):
        toks.append((m.start(), "ann", m.group(1)))
    toks.sort()

    pairs: list[tuple[str, str]] = []
    last_id, seen = None, set()
    for _, kind, val in toks:
        if kind == "id":
            last_id = val
        elif last_id and (last_id, val) not in seen:
            seen.add((last_id, val))
            pairs.append((last_id, val))

    out = []
    for gid, fn in pairs:
        url = f"{base}/userdata/public/gfx/{gid}/{urllib.parse.quote(fn)}"
        if check and not _reachable(url):
            continue
        out.append({"id": gid, "filename": fn, "url": url})
    return out
