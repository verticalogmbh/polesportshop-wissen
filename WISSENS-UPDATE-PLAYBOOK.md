# Wissens-Update-Playbook

**Stand:** v1.0, 2026-05-18 (Berlin)
**Zweck:** Operative Spec für Cowork-getriebene Wissens-Update-Builds. Wird bei Trigger „Verarbeite Wissens-Update für v<NEW>..." aus dem jüngsten Snapshot geladen und ausgeführt — analog zu `run_brief_daten.md` für Daten-Läufe.
**Bezug:** Charter-Prinzip 12 (File-Header-Versionierungs-Disziplin), E47 (Snapshot-Architektur), E61/E62 (Konstanten/Spec-Caching), E85 (dieses Pattern als Standard), E86 (SemVer-Konvention).
**Token-Effizienz:** Faktor 15-20 günstiger als Claude.ai-MCP-direkt-Schreiben (Dateiinhalt wird nicht durch Antwort-Stream geschoben). Bewährt im v1.17-Build (mehrere Stunden autonom, byte-identisch verifiziert, Self-Check PASS).

---

## 1. Trigger-Erkennung

Trigger-Phrasen die diesen Playbook aktivieren:
- „Verarbeite Wissens-Update für v<NEW>..."
- „Baue Snapshot v<NEW>..."
- „Wissens-Build v<NEW>..."

Bei diesen Triggern: lese diesen Playbook + den Auftrag aus dem Chat. Der Auftrag definiert den **Scope** (welche Files modifiziert, welche neu, welche unverändert). Der Playbook definiert das **Wie**.

Bei Daten-Pipeline-Triggern („Verarbeite neue Artikel von X...") lädt Cowork stattdessen `run_brief_daten.md` (E68).

---

## 2. 12-Stage-Build-Pattern

Stage-Reihenfolge linear, keine Querverweise. Jede Stage hat einen klaren Output, der von der nächsten Stage konsumiert wird.

| Stage | Was | Output |
|---|---|---|
| 1 | Snapshot-Resolution + lokales Caching | `/home/claude/wissens_in/` befüllt |
| 2 | Python-Inventur (Header-Parse, Bytes, Hashes) | `inventur.json` |
| 3 | Workspace-Vorbereitung + unveränderte Files kopieren | `/home/claude/wissens_out/` Basis |
| 4 | Neue Files schreiben | Neue Files in `wissens_out/` |
| 5 | Modifizierte Files schreiben (mit Header-Bump) | Modifizierte Files in `wissens_out/` |
| 6 | (Falls Split) Cluster-Mapping + neue Cluster-Files | Cluster-Files in `wissens_out/` |
| 7 | Snapshot-Folder in Drive anlegen | Neue Folder-ID |
| 8 | SPEC_KONSTANTEN-Sektionen 13/14 anpassen (falls neue Files / E-Nummern) | aktualisiertes SPEC_KONSTANTEN |
| 9 | Resolver-Specs anpassen (cowork_custom_instructions, Projekt-Anweisungen) | aktualisierte Resolver-Files |
| 10 | Self-Check (Python-Skript) mit WSC-1 bis WSC-17 | `selfcheck.json`, PASS/FAIL |
| 11 | Manifest schreiben | `_MANIFEST.md` |
| 12 | Upload aller modifizierten/neuen Files via Drive-MCP, dann Report | Lauf-Bericht für Tjorben |

---

## 3. Tool-Patterns

### 3.1 Sandbox-Pfad-Trick für Files >40 KB

`download_file_content` hat Token-Limit (Cowork-Read-Tool ~25k Token). Bei größeren Files spiegelt der MCP-Connector das Result-File unter `/private/tmp/mcp-*-read_file_content-*.txt` als JSON mit base64-Payload (Stand 2026-05-18; früher `/sessions/.../mnt/.claude/projects/.../tool-results/`). Workflow:

1. `download_file_content` aufrufen — auch wenn es Token-Limit ausgibt, das File ist auf Disk.
2. Per `find /private/tmp -name "mcp-*-read_file_content-*.txt" -mmin -2` aufspüren.
3. Python: `with open(path) as f: data = json.load(f); content = base64.b64decode(data['content']).decode('utf-8')`.
4. Resultat lokal cachen, kein Chat-Dump.

### 3.2 Subagent für File-Operations >40 KB

Subagent-Calls dumpen nicht in den Main-Context. Nutzen für: Initial-File-Extraktion großer Files, große Cluster-Splits, Resolver-Specs Download+Modify+Upload. Subagent-Prompt muss self-contained sein:
- Präziser File-Pfad (volle ID + Titel)
- Explizite Tool-Wahl
- Erwartete Anzahl an Output-Files (für Anzahl-Match-Check, verhindert Duplikat-Bugs)

### 3.3 `base64Content` als Default für Drive-Uploads

`textContent`-Uploads strippen das letzte `\n` und erzeugen 1-Byte-Diff zur Quelle. Bei strikter Byte-Match-Verifikation (WSC-7) ist das ein Fail. Daher: immer `base64Content` mit `contentMimeType` setzen.

Beispiel-Python:
```python
import base64
content_b64 = base64.b64encode(file_bytes).decode('ascii')
# Dann via Drive-MCP: create_file(base64Content=content_b64, contentMimeType='text/markdown', ...)
```

### 3.4 Drive-MCP hat KEINE Delete-Operation

Bei Upload-Abbruch oder fehlgeschlagenem Versuch bleiben Karteileichen liegen. Daher:
- **Pre-Validation:** vor zweitem Upload-Versuch lokale Datei-Größe gegen base64-Dekoder-Größe prüfen
- **Karteileichen ins Manifest** als Manual-Cleanup-Action mit Drive-ID
- **Nie versuchen** über Workarounds zu löschen

---

## 4. Anti-Patterns (lessons learned, vermeiden)

- **Karteileiche durch Subagent-Stub-Upload:** Subagent hat im v1.17-Build einen 2,3-KB-Stub statt Vollinhalt hochgeladen. Mitigation: Pre-Validation der Payload-Größe vor jedem `create_file`-Call.
- **LIVE-TRIAL fast vergessen:** Subagent-Prompt hatte zwei Dateien als Duplikat (Copy-Paste-Bug). Mitigation: Subagent muss Anzahl-Match prüfen (Erwartung vs. tatsächlich).
- **Trailing-Newline-Strip:** `textContent`-Upload → 1-Byte-Diff. Mitigation: `base64Content` als Default.
- **Token-Limit bei download_file_content für File >50 KB.** Mitigation: Sandbox-Pfad-Trick (3.1).
- **UI-Drift Cowork-Custom-Instructions ↔ Drive-Backup:** nach jedem Snapshot-Build expliziter Schritt „UI-Custom-Instructions updaten" mit Verifikations-Pflicht.
- **Header-Bump-Vergessen:** Im v1.17-Build wurden 4 Files modifiziert ohne File-Header-Bump. Mitigation: Versionierungs-Policy (Sektion 5) + WSC-17.

---

## 5. Versionierungs-Policy (E86)

### 5.1 Snapshot-Version vs. File-Header sind entkoppelt

- **Snapshot-Version** = Folder-Name `Version_YYYY-MM-DD_HHMMSS` = Stand des gesamten Sets
- **File-Header** `**Stand:** v1.X` = Inhalts-Stand der einzelnen Datei

Folge: ein File im Snapshot v1.18 kann File-Header v1.15.1 haben (Patch-Bump aus v1.17-Touch), während ein anderes File auf v2.0 ist.

### 5.2 Bump-Konvention (SemVer-style)

| Bump-Typ | Wann | Beispiel |
|---|---|---|
| **Patch** (v1.15 → v1.15.1) | reine Referenz-/Cross-Verweis-Updates ohne Inhalts-Änderung | „verweis von alter Sektion 12 auf neue Sektion 14" |
| **Minor** (v1.15 → v1.16) | Inhalts-Updates, neue Sektionen, neue Regeln | „neuer Eintrag F5, neue Self-Check-Punkte" |
| **Major** (v1.15 → v2.0) | strukturelle Umbauten, Architektur-Pivots | „Cluster-Split: Monolith in 6 Cluster" |

### 5.3 Edge-Case: nur-mit-mitgenommen ≠ Bump

Wenn ein File ohne Modifikation aus dem Vorgänger-Snapshot ¼bernommen wird (Stage 3.2 Kopie): **kein Bump**. Der Header bleibt unverändert. Im Manifest wird das File als „unverändert kopiert" gelistet.

Wenn auch nur eine Referenz/ein Cross-Verweis aktualisiert wird: **Patch-Bump**.

### 5.4 Verifikation

Vor Manifest-Schreibung prüft Self-Check-Punkt WSC-17: Alle im Manifest als „modifiziert" gelisteten Files haben gegenüber dem Vorgänger-Snapshot einen Header-Bump erhalten. Diff-Check via Python.

---

## 6. Self-Check-Liste (WSC-1 bis WSC-17)

Pflicht vor Manifest-Schreibung. Implementiert als Python-Skript `selfcheck.py` unter `/home/claude/`. Output: `selfcheck.json` mit PASS/FAIL pro Punkt.

1. **WSC-1 — Größen-Limit ≤ 50 KB Hard-Limit:** Alle Files unter Limit, außer dokumentierte Known-Exceptions.
2. **WSC-2 — Append-/Patch-File-Verbot:** Keine `*_Append*` oder `*_Patch*`-Files im Snapshot.
3. **WSC-3 — SNAPSHOT_KNOWLEDGE_FILES-Match:** Folder-Inhalt matched die in SPEC_KONSTANTEN Sektion 13 gelistete File-Liste exakt.
4. **WSC-4 — Cross-References zu ARCHIV:** Alle E-Nummer-Verweise in den Cluster-Files sind in `ENTSCHEIDUNGS-LOG-ARCHIV.md` vorhanden.
5. **WSC-5 — Neue Sektionen in SPEC_KONSTANTEN vorhanden:** Falls Sektion 13/14 erweitert wurde, sind die neuen Einträge da.
6. **WSC-6 — Kein alter Monolith:** Falls Cluster-Split passierte, das alte Monolith-File ist nicht im Folder.
7. **WSC-7 — Byte-Identität bei kopierten Files:** Hash gegen Vorgänger-Snapshot stimmt für unveränderte Files.
8. **WSC-8 — Build-Target ≤ 40 KB für neue/modifizierte Files:** Sonst Cluster-Split planen.
9. **WSC-9 — UTF-8-Sanity:** Kein BOM-Bruch (außer für CSVs), kein Encoding-Drift.
10. **WSC-10 — Manifest enthält alle Files mit Hashes:** SHA256 für jedes Wissens-File im Snapshot.
11. **WSC-11 — Manifest-Build-Trail vollständig:** Sektionen „neu / modifiziert / unverändert / nicht mehr existiert" gefüllt.
12. **WSC-12 — Known-Exceptions dokumentiert:** Files > 50 KB mit Begründung + geplanter Split-Snapshot.
13. **WSC-13 — Cleanup-Aktionen vermerkt:** Karteileichen für Tjorben aufgelistet mit Drive-IDs.
14. **WSC-14 — Notes ans Claude.ai-Projekt:** Spec-Feedback, Tool-Anomalien, neue Drift-Pfade.
15. **WSC-15 — Snapshot-Folder eindeutig:** Sekundengenauer Timestamp im Format `Version_YYYY-MM-DD_HHMMSS`, kein Konflikt.
16. **WSC-16 — Anzahl Files = erwartet:** N Wissens-Files + 1 Manifest = (N+1) im Folder.
17. **WSC-17 — File-Header-Bump-Pflicht (NEU E86, ab v1.18):** Alle im Manifest als „modifiziert" gelisteten Files haben gegenüber Vorgänger einen Header-Bump (Patch/Minor/Major gemäß 5.2).

**Fails sind blockierend** — bei FAIL: korrigieren und neu validieren, **nicht uploaden**. Warnings dokumentieren im Manifest unter „informational Warnings".

---

## 7. Manifest-Spec

Pflichtsektionen in jedem `_MANIFEST.md`:

1. **Header** — Snapshot-Name, Stand, Folder-ID, Parent-ID, Vorgänger-Snapshot
2. **Build-Trail** — Auftrag (was Claude.ai-Projekt aufgegeben hat), Resultat (was passiert ist), Build-Modus (Bootstrap/Standard)
3. **Was neu generiert wurde** — Liste mit File-Name + Zweck
4. **Was modifiziert wurde** — Liste mit File-Name + Änderungs-Typ (Patch/Minor/Major) + Begründung
5. **Was unverändert kopiert wurde** — Liste
6. **Was nicht mehr existiert** — Liste (bei Cluster-Splits oder File-Entfernungen)
7. **File-Liste mit Drive-IDs, Sizes, SHA256-Hashes** — Tabelle
8. **Anzahl-Marker** — Wissens-Files + Manifest = Total
9. **Self-Check-Ergebnis** — Status (PASS/FAIL), pro WSC-Punkt
10. **Known-Exceptions / Geplante Folge-Splits**
11. **Manuelle Cleanup-Aktionen für Tjorben** (Karteileichen-Drive-IDs)
12. **Notes ans Claude.ai-Projekt** — Spec-Feedback, Anomalien

---

## 8. Output-Format

Am Ende des Builds:
- Lokale Files: alle in `/home/claude/wissens_out/`
- Upload: alle modifizierten/neuen Files via Drive-MCP nach `Version_<jetzt>/`
- Unveränderte Files: per Drive-MCP `copy_file` direkt in den neuen Folder (kein lokaler Roundtrip)
- Lauf-Bericht im Workspace + via `present_files` an Tjorben

---

## 9. Bootstrap-Hinweis

Dieser Playbook ist **selbst entstanden durch v1.18** (Bootstrap). Ab v1.19 ist das Pattern das Standardverfahren — der Trigger im Chat bleibt knapp und referenziert diesen Playbook, statt den vollen Build-Plan zu duplizieren.
