"""
Pricing (P3, run_brief Stage 4).

Marge-Modell (E104, 2026-06-25): Brutto-VK so, dass die JTL-Marge „Gewinn %"
(Netto-VK gegen die GLD) = MARGE_ZIEL (40 %, Haus-Standard). Netto-VK = GLD/(1-Marge),
Brutto = *MwSt -> kaufm. ,90 -> Charm. Der VK folgt der GLD (keine EK/VK-Puffer mehr).
GLD = EK_eur + Aufschlag (EU +0,50 / Nicht-EU +2,30, E103). Löst „EK×2" (~50 %) ab.

EK kommt aus einer EK-Liste/Rechnung (CSV in pipeline/EK_input/), gekeyt auf
(modell_basis, garment_type, farbe). Fehlt für einen Vater der EK -> STOPP
(Charter-Prinzip 10): nicht raten, sondern als 'missing' melden.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

from . import constants as C
from .model import Vater


def _key(modell: str, typ: str, farbe: str) -> tuple[str, str, str]:
    return (modell.strip().lower(), typ.strip().lower(), (farbe or "").strip().lower())


def round_vk_90(value: float) -> float:
    """Nächstes X,90 (kaufmännisch, Ties auf-runden)."""
    n = math.floor(value - 0.9 + 0.5 + 1e-9)  # round-half-up von (value-0.9)
    return round(n + 0.9, 2)


def charm_vk(vk: float) -> float:
    """Verkaufspsychologische Korrektur (E101): runde Zehner-Beträge vermeiden.
    Endet der Euro-Betrag auf 0 (z.B. 40,90 / 50,90), 1 € runter -> X9,90 (39,90 / 49,90).
    Alle anderen Endungen (46,90, 62,90) bleiben."""
    euro = int(round(vk, 2))
    return round(vk - 1.0, 2) if euro % 10 == 0 else round(vk, 2)


def load_ek_csv(path: Path) -> dict[tuple[str, str, str], float]:
    ek: dict[tuple[str, str, str], float] = {}
    with path.open("r", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter=";"):
            ek[_key(row["modell"], row["typ"], row.get("farbe", ""))] = float(
                str(row["ek_netto"]).replace(",", ".")
            )
    return ek


def vk_aus_marge(gld: float, marge_ziel: float = C.MARGE_ZIEL) -> float:
    """Brutto-VK so, dass die JTL-Marge (Netto-VK gegen GLD) = marge_ziel (E104).
    Netto-VK = GLD/(1-marge); Brutto = *MwSt -> kaufm. ,90 -> Charm (keine runden Zehner)."""
    netto_vk = gld / (1.0 - marge_ziel)
    return charm_vk(round(round_vk_90(netto_vk * C.MWST_FAKTOR), 2))


def apply_pricing(vaeter: list[Vater], ek_map: dict[tuple[str, str, str], float],
                  fx_to_eur: float = 1.0,
                  gld_aufschlag: float = C.GLD_AUFSCHLAG_NICHTEU_EUR,
                  marge_ziel: float = C.MARGE_ZIEL):
    """
    Setzt ek_netto (in EUR), gld + vk_brutto auf jedem Vater, für den ein EK existiert.
    fx_to_eur: Umrechnungsfaktor falls Rechnung nicht in EUR (z.B. USD 0.8612).
    GLD = EK_eur + gld_aufschlag (EU +0,50 / Nicht-EU +2,30, E103) — die landed-cost-Basis.
    Brutto-VK = Marge-Modell (E104): aus der GLD auf marge_ziel (40 %) gerechnet -> der VK
    folgt der GLD. Keine separaten EK/VK-Puffer mehr (die GLD trägt Zoll/Versand). -> (priced, missing).
    """
    priced, missing = [], []
    for v in vaeter:
        ek = ek_map.get(_key(v.modell_basis, v.garment_type, v.farbe_raw))
        if ek is None:
            missing.append(v)
            continue
        ek_eur = round(ek * fx_to_eur, 2)
        v.ek_original = round(ek, 2)   # Lieferanten-Währung (z.B. AUD) -> Lieferanten-Netto-EK
        v.ek_netto = ek_eur            # EUR -> Basis des GLD
        v.gld = round(ek_eur + gld_aufschlag, 2)   # Ø-EK/GLD inkl. EU/Nicht-EU-Kosten-Aufschlag (E103)
        v.vk_brutto = vk_aus_marge(v.gld, marge_ziel)   # VK aus GLD auf Ziel-Marge (E104)
        priced.append(v)
    return priced, missing
