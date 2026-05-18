# Cowork-Anweisung: Bildpipeline polesports

> ## 🗄️ ARCHIVIERT — nicht aktiv ausgeführt (E63, 2026-05-16)
>
> Die Bildpipeline läuft **nicht** mehr automatisch. Tjorben pflegt Bilder manuell in WaWi.

**Stand:** v2.0, 2026-05-18 (Stub-Reduktion im v1.20-Refactor E91: Voll-Spec von 43 KB auf ~2 KB reduziert; Detail-Spezifikation für Reaktivierung aus Git-History des `v1.19`-Tags rekonstruierbar). · **Vorheriger Stand:** v1.6, 2026-05-16 (Voll-Spec im `v1.19`-Tag erhalten).

---

## Status

- **Pipeline:** DEAKTIVIERT seit 2026-05-16 (E63). Bild-Spalten in Stammdaten-CSV bleiben leer (Schema-Konformität via 10 Bild-Spalten erhalten, E46).
- **Workflow im Pilot:** Tjorben pflegt Bilder pro Artikel manuell in WaWi-UI (Drag-and-Drop pro Artikel). Re-Aktivierung der Pipeline hängt am Architektur-Refactor (BACKLOG-Cluster B36-B40).
- **R2-Storage:** vorhandene Bilder bleiben auf Cloudflare R2 erhalten (`polesportshop-images`-Bucket, Prefix pro Lieferant). Migrations-Stand: HotCakes Arachne Bottom Black + Originale 2026-05-15 erfolgreich.
- **Mapping-Felder eingefroren:** `crop_profile`, `pose_sort`, `r2_prefix` in `lieferanten_mapping.yaml` bleiben für spätere Reaktivierung erhalten. Werden aktuell nicht gelesen.

## Trigger-Verhalten in Cowork

Bei Trigger „Verarbeite Bilder von <LIEFERANT>...":
- User informieren: „Bildpipeline aktuell archiviert (E63). Bilder pflegst du manuell in WaWi."
- Verweis auf BACKLOG-Cluster B36-B40 für Klärung der Reaktivierungs-Bedingungen.
- Kein Pipeline-Lauf, kein partieller Output, keine R2-Operations.

## Reaktivierungs-Pfad

Wenn Reaktivierung gewünscht (Lieferanten-Volumen-Wachstum, Bilder-Architektur-Refactor abgeschlossen):

1. **Voll-Spec rekonstruieren** aus Git-History: `git show v1.19:cowork_anweisung_bildpipeline.md > /tmp/bildpipeline_v1.6.md`. v1.6-Stand enthält: Stages 1-7 (Crawl → Download → Vision-Klassifikation → Crop → R2-Upload → Index-HTML), R2-Mechanik via boto3 + Drive-Credentials (E43), Crop-Profile (fashion 2:3 / tech 1:1, E45), Pose-Sortierung via Vision (Hero/Back/Side), Anti-Bot-Pattern, Original-Index-HTML pro Lieferant.
2. **BACKLOG-Cluster B36-B40 review** für Architektur-Entscheidungen (Worker-Proxy für R2, Vision-API-Anbieter, Bild-Größen-Cap-Politik).
3. **Neuer Wissens-Update-Build** mit Voll-Spec als neuer File-Version v2.X (Major-Bump weil reaktiviert) und entsprechender Charter-Anpassung.

## Verwandte Dokumente

- `ENTSCHEIDUNGS-LOG-BILDPIPELINE.md` — Architektur-Entscheidungen E10–E12, E44–E46, E60, E63 (Archivierung), E70
- `BACKLOG.md` — aktiver Bilder-Architektur-Refactor-Cluster B36-B40 (Bilder-Workflow, R2-Performance, Vision-API-Eval, Filename-Konventionen, manueller Pflege-Overhead)
- `BACKLOG-ARCHIV.md` — historische Bilder-Backlog-Punkte falls verschoben
- `lieferanten_mapping.yaml` — eingefrorene Felder `crop_profile`, `pose_sort`, `r2_prefix`
- `SPEC_KONSTANTEN.md` Sektion 13 — File-Index zeigt dieses File als Stub

## Hinweis für Cowork

Diese Datei wird **nicht in Stage 0** geladen. Wenn lazy-geladen während eines Daten-Pipeline-Laufs (z.B. weil ein Trigger Bildpipeline-Bezug suggeriert): Stub erkennen, User auf Archivierung verweisen, keinen Workaround starten.
