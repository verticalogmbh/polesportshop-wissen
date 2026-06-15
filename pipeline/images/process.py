"""
Bildverarbeitung (P8, SPEC cowork_anweisung_bildpipeline E45/E60).

Crop-Profil 'fashion': 2:3, 1000x1500, top_bias 0.3, LANCZOS.
Kompression: JPEG, Quality iterativ 95 -> Floor 30, bis < 100 KB.
Reihenfolge: manufacturer_order (Shopify-Bildreihenfolge), keine Vision.
Magic-Byte-Detection für Original-Extension.
"""
from __future__ import annotations

import io
import urllib.request
from dataclasses import dataclass

from PIL import Image

_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

CROP_PROFILES = {
    "fashion": {"ratio": (2, 3), "size": (1000, 1500), "top_bias": 0.3},
    "tech":    {"ratio": (1, 1), "size": (1200, 1200), "top_bias": 0.0},
}
MAX_BYTES = 100 * 1024
Q_START, Q_FLOOR, Q_STEP = 95, 30, 5

_MAGIC = [
    (b"\xff\xd8\xff", "jpg"), (b"\x89PNG\r\n\x1a\n", "png"),
    (b"GIF87a", "gif"), (b"GIF89a", "gif"),
    (b"RIFF", "webp"),  # RIFF....WEBP
]


@dataclass
class ProcessedImage:
    index: int
    jpg_bytes: bytes
    orig_bytes: bytes
    orig_ext: str
    final_quality: int
    final_kb: float


def _magic_ext(b: bytes) -> str:
    for sig, ext in _MAGIC:
        if b.startswith(sig):
            if ext == "webp" and b[8:12] != b"WEBP":
                continue
            return ext
    return "bin"


def download(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def crop_resize(img: Image.Image, profile: str) -> Image.Image:
    p = CROP_PROFILES[profile]
    tw, th = p["ratio"]
    target = tw / th
    w, h = img.size
    if w / h > target:                      # zu breit -> Seiten beschneiden (zentriert)
        nw = int(round(h * target))
        left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:                                   # zu hoch -> Höhe beschneiden mit top_bias
        nh = int(round(w / target))
        top = int(round((h - nh) * p["top_bias"]))
        img = img.crop((0, top, w, top + nh))
    return img.resize(p["size"], Image.LANCZOS)


def compress_jpeg(img: Image.Image) -> tuple[bytes, int]:
    if img.mode != "RGB":
        img = img.convert("RGB")
    q = Q_START
    while True:
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=q, optimize=True)
        data = buf.getvalue()
        if len(data) <= MAX_BYTES or q <= Q_FLOOR:
            return data, q
        q -= Q_STEP


def process_vater(image_urls: list[str], profile: str) -> list[ProcessedImage]:
    """Bilder in Shopify-Reihenfolge (manufacturer_order) verarbeiten."""
    out = []
    for i, url in enumerate(image_urls, start=1):
        raw = download(url)
        img = Image.open(io.BytesIO(raw))
        proc = crop_resize(img, profile)
        jpg, q = compress_jpeg(proc)
        out.append(ProcessedImage(index=i, jpg_bytes=jpg, orig_bytes=raw,
                                  orig_ext=_magic_ext(raw), final_quality=q,
                                  final_kb=round(len(jpg) / 1024, 1)))
    return out
