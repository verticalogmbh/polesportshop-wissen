"""
CSV 2: Variationen (12 Spalten, run_brief §5).
Eine Zeile pro Größen-Variante des Vaters. Darstellungsform DROPDOWN.
Variationsname lokalisiert (Größe/Size/Taille/Taglia/Talla); Werte universal.
"""
from __future__ import annotations

from .. import spec, constants as C
from ..model import Vater


def _rank(groesse: str) -> int:
    return C.GROESSEN_RANG.index(groesse) if groesse in C.GROESSEN_RANG else -1

COLUMNS = [
    "Artikelnummer", "Variationsname", "Darstellungsform", "Variationswertname",
    "Global-Englisch: Variationsname", "Global-Englisch: Variationswertname",
    "Global-Französisch: Variationsname", "Global-Französisch: Variationswertname",
    "Global-Italienisch: Variationsname", "Global-Italienisch: Variationswertname",
    "Global-Spanisch: Variationsname", "Global-Spanisch: Variationswertname",
]

VARIATIONSNAME = {"de": "Größe", "en": "Size", "fr": "Taille", "it": "Taglia", "es": "Talla"}


def build_rows(vaeter: list[Vater], supplier: dict, run_date: str) -> list[dict]:
    rows: list[dict] = []
    for v in vaeter:
        vnr = spec.vater_artnr(v.garment_type, v.modell_basis, v.farbe_raw)
        # Absteigend ausgeben (L,M,S,XS): JTL-Ameise kehrt die Import-Reihenfolge
        # um, sodass der Shop aufsteigend XS->L anzeigt (Tjorben-Beobachtung 2026-06-15).
        for k in sorted(v.kinder, key=lambda x: _rank(x.groesse), reverse=True):
            rows.append({
                "Artikelnummer": vnr,
                "Variationsname": VARIATIONSNAME["de"], "Darstellungsform": "DROPDOWN",
                "Variationswertname": k.groesse,
                "Global-Englisch: Variationsname": VARIATIONSNAME["en"],
                "Global-Englisch: Variationswertname": k.groesse,
                "Global-Französisch: Variationsname": VARIATIONSNAME["fr"],
                "Global-Französisch: Variationswertname": k.groesse,
                "Global-Italienisch: Variationsname": VARIATIONSNAME["it"],
                "Global-Italienisch: Variationswertname": k.groesse,
                "Global-Spanisch: Variationsname": VARIATIONSNAME["es"],
                "Global-Spanisch: Variationswertname": k.groesse,
            })
    return rows
