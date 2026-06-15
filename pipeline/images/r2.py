"""
R2-Upload (P9, SPEC E43/E44). S3-kompatibel via boto3.

Pro Bild zwei Objekte:
  <prefix>/<artnr>-<N>.jpg              verarbeitetes Shop-Bild
  originals/<prefix>/<artnr>-<N>.<ext>  Original (Magic-Byte-Extension)
Public-URL = R2_PUBLIC_BASE/<prefix>/<artnr>-<N>.jpg.
Idempotent: gleicher Key wird überschrieben (kein Duplikat). 3 Retries.

Credentials: config.r2_credentials() (env oder pipeline/.secrets/...), nie geloggt.
"""
from __future__ import annotations

import time

import boto3
from botocore.config import Config as BotoConfig

from .. import config
from .process import ProcessedImage

_CONTENT_TYPE = {"jpg": "image/jpeg", "png": "image/png", "webp": "image/webp",
                 "gif": "image/gif", "heic": "image/heic", "bin": "application/octet-stream"}
_CACHE = "public, max-age=2592000"


def _client():
    creds = config.r2_credentials()
    return boto3.client("s3", config=BotoConfig(retries={"max_attempts": 3, "mode": "standard"}),
                        **creds)


def _put(client, key: str, body: bytes, content_type: str):
    for attempt in range(3):
        try:
            client.put_object(Bucket=config.R2_BUCKET, Key=key, Body=body,
                              ContentType=content_type, CacheControl=_CACHE)
            return
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def upload_vater(client, prefix: str, artnr: str, images: list[ProcessedImage]) -> list[str]:
    """Lädt verarbeitete + Original-Bilder hoch. Gibt Public-URLs (verarbeitet) zurück."""
    urls = []
    for pi in images:
        fname = f"{artnr}-{pi.index}"
        _put(client, f"{prefix}/{fname}.jpg", pi.jpg_bytes, "image/jpeg")
        _put(client, f"originals/{prefix}/{fname}.{pi.orig_ext}", pi.orig_bytes,
             _CONTENT_TYPE.get(pi.orig_ext, "application/octet-stream"))
        urls.append(f"{config.R2_PUBLIC_BASE}/{prefix}/{fname}.jpg")
    return urls


def make_client():
    return _client()
