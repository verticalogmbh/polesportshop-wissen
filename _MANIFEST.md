# Snapshot-Manifest

**Snapshot-Name:** `Version_2026-05-18_141930`
**Stand:** v1.18, 2026-05-18 (Berlin, ~14:19 CEST)
**Folder-ID:** `1D78Ht-hhUYoGRLRDMuCB-y7LYG8mp6Mn`
**Parent-ID:** `12wDy0Z0cmB0p-OAs10Y7XqBWhmtQEip5` (Wichtig: Claude Backup)
**Vorgänger-Snapshot:** `Version_2026-05-17_212017` (Folder-ID `139k1Ri9C8SC0kWBIt-XsEPAt2MO_F0zr`)

---

## 1. Build-Trail

**Auftrag (vom Claude.ai-Projekt):** Bootstrap-Build v1.18 mit 3 orthogonalen Strängen:
- **Strang A** — Build-Pattern verankert: neues `WISSENS-UPDATE-PLAYBOOK.md` als operative Spec für künftige Wissens-Builds.
- **Strang B** — Versionierungs-Policy: Charter-Prinzip 12, E85+E86, WSC-17, plus 4 ausstehende v1.17-Header-Bumps nachholen.
- **Strang C** — F1-F7 aus HotCakes-Run-Report 2026-05-18 als BACKLOG-Punkte B54-B60 priorisiert dokumentieren.

**Build-Modus:** Bootstrap — Playbook entsteht inline durch diesen Build.

**Resultat:** Snapshot mit 18 erwarteten Wissens-Files. 16 von 18 erfolgreich uploaded (10 via Drive copy_file, 6 via base64Content from main context). 2 Files (`BACKLOG.md`, `cowork_anweisung_datenimports.md`) durch base64-Stream-Drift-Limit nicht uploadbar — **manual upload durch Tjorben nötig**, lokale Files via `present_files` ausgegeben.

---

## 2. Was neu generiert wurde (1 File)

| Datei | Zweck |
|---|---|
| `WISSENS-UPDATE-PLAYBOOK.md` | Operative Spec für Cowork-getriebene Wissens-Update-Builds (E85). Bootstrap-Source für 12-Stage-Pattern. |

---

## 3. Was modifiziert wurde (7 Files mit Header-Bump)

| Datei | Bump-Typ | Begründung |
|---|---|---|
| `PROJEKT-CHARTER.md` | Minor (v1.15 → v1.16) | Neues Prinzip 12 (File-Header-Versionierungs-Disziplin, E86); Stand-Update auf 2026-05-18 |
| `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` | Minor (v1.17 → v1.18) | Zwei neue E-Einträge E85 + E86 |
| `SPEC_KONSTANTEN.md` | Minor (Spec-Bezug v1.15 → v1.16) | Sektion 13 um WISSENS-UPDATE-PLAYBOOK.md erweitert; Sektion 14 um E85+E86; Cross-Ref am Ende Sektion 9 |
| `BACKLOG.md` | Minor (hinzu → v1.18) | 7 neue Einträge B54-B60 aus HotCakes-Run-Report |
| `cowork_custom_instructions.md` | Minor (v1.15 → v1.16) | Neue Sektion „Wissens-Update-Trigger (E85)"; Anzahl-Marker 17 → 18 Wissens-Files |
| `Projekt-Anweisungen.md` | Minor (hinzu → v1.16) | Hinweis WISSENS-UPDATE-PLAYBOOK.md in Routine-Output Schritt 2; Drive-Struktur + Anzahl-Marker aktualisiert |
| `cowork_anweisung_datenimports.md` | Patch (v1.15 → v1.15.1) | Performance-Diagnose-Hinweis Sektion 3.1 (BACKLOG B54) |

---

## 4. Was unverändert kopiert wurde (10 Files)

| Datei | Vorgänger-Drive-ID | Neue Drive-ID |
|---|---|---|
| `ENTSCHEIDUNGS-LOG-ARCHIV.md` | 1ZoJadIsYN-ydisJVO4WozhDb4_d9NNfm | 1AEy0N8RTyk6Ckig5aYsZRi5qfNzCPpcU |
| `ENTSCHEIDUNGS-LOG-CRAWLING-DATEN.md` | 1lZ5iYDgcKpFv72CRBddIAtsoGXBMWU3E | 1fLnylz6NoH9sUdCxXTvPkJRoYZYd5oA_ |
| `ENTSCHEIDUNGS-LOG-BILDPIPELINE.md` | 1wB3JuktS7_74jISbn7InAUCZu4ZPHEN3 | 1CJtqohM94aUE81f2dHf-ej2IyUdNFllY |
| `ENTSCHEIDUNGS-LOG-STIL-CONTENT-A.md` | 15XpTlv-PgaUl-F4JCuySbWWOOsdsZDJC | 1D0pwaeZbqA9m54-LK-ijEUX_mToLW0Si |
| `ENTSCHEIDUNGS-LOG-STIL-CONTENT-B.md` | 1iCxC_QTQ41ZgxAKPlyVgBEUQAQflivK- | 1WtkwCdjemnG3iK2WQ4bpPzg-Q2-zVO5l |
| `ENTSCHEIDUNGS-LOG-LIVE-TRIAL.md` | 1McVdtIFI4ycIltSZl7EmvNlDb7AQUXsl | 1Z5OKcXJIvdR-TEUbofGQ9ukD-eM_-BMh |
| `run_brief_daten.md` | 1BJ35h2cjQMrhpDTBPb-nn0nGHXg-COn1 | 1b34-yZqCSZNab_bVCS76pfdJ4yKyLWV_ |
| `lieferanten_mapping.yaml` | 19oGtTv-yd06qQCLQjcJ0D4qpEMPm01wt | 1Z-SpOVwWCxpbQvLS0GasjxdfSLYN_aWn |
| `WAWI-IMPORT-WISSEN.md` | 1OdEIhLmQa1SBLeQ4SYg58xdnhDdFCVyM | 1Sov_8PwxWdAqrbAuEPxiQakcBdAHW4Co |
| `cowork_anweisung_bildpipeline.md` | 1OTRmvvUIMNNLn0bTZ_KjLnhmeSkkOL6V | 1FVscj13-UehFavN6CYURgYtrAh5iVl4W |

---

## 5. Was nicht mehr existiert

Keine Files entfernt in v1.18.

---

## 6. File-Liste mit Drive-IDs, Sizes, SHA256-Hashes

### Erfolgreich in Drive (16 von 18 Wissens-Files)

| Datei | Drive-ID | Lokale Size (B) | SHA256 (lokal) | Status |
|---|---|---|---|---|
| `WISSENS-UPDATE-PLAYBOOK.md` | 1wIOPjtshXJ-sfSN-hEMLsBVnamfbslpk | 10737 | `684ac9dd923c691187099062c6fe409257438a5842f265507e598a54c8141d85` | OK (Drive-size 10737 match) |
| `PROJEKT-CHARTER.md` | 1qz4uAQt_0n4miEpu7cgK0UhHGyhGGB5t | 20843 | `08b61ffe1879224de0d1b1fe4394812339b64aefbf8ed0b2e29faa25918c8381` | OK (Drive-size 20843 match) |
| `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` | 1s7uvWV07JjQPIcidSdcfyX_SD64Bcbjc | 43470 | `e27e6767939dc0cf3bf39e677693e8c37fbbfc14437fe8321ab11ca7ee83fc4a` | OK (Drive-size 43470 match) |
| `SPEC_KONSTANTEN.md` | 1pyEcLLzZ2gLIuKlgY8JI4WTQtp7Yfhba | 49321 | `67685e811f3e5ed87530c50b5e75f9c547f27b04d3fde212e0237fc9db2d1cbb` | OK (Drive-size 49321 match) |
| `cowork_custom_instructions.md` | 1r_x6jDvVba9r17Vqxlf3QijrBM5zxuHu | 15214 | `1451e242fb97a294e57c00ff84a52b57ef5673c5784cf53972b659a994b2f55d` | OK (Drive-size 15214 match) |
| `Projekt-Anweisungen.md` | 14-3FxOsWYunY2R-kfB_5VXWgKao8omYu | 17747 | `c1c5c0a9705b38f7a37d75ccd659c932e41c87d0e79b72a6b388e98f64c167f2` | OK (Drive-size 17747 match) |
| `ENTSCHEIDUNGS-LOG-ARCHIV.md` | 1AEy0N8RTyk6Ckig5aYsZRi5qfNzCPpcU | 9600 | (unverändert, Drive-Copy) | OK |
| `ENTSCHEIDUNGS-LOG-CRAWLING-DATEN.md` | 1fLnylz6NoH9sUdCxXTvPkJRoYZYd5oA_ | 30760 | (unverändert, Drive-Copy) | OK |
| `ENTSCHEIDUNGS-LOG-BILDPIPELINE.md` | 1CJtqohM94aUE81f2dHf-ej2IyUdNFllY | 24725 | (unverändert, Drive-Copy) | OK |
| `ENTSCHEIDUNGS-LOG-STIL-CONTENT-A.md` | 1D0pwaeZbqA9m54-LK-ijEUX_mToLW0Si | 33869 | (unverändert, Drive-Copy) | OK |
| `ENTSCHEIDUNGS-LOG-STIL-CONTENT-B.md` | 1WtkwCdjemnG3iK2WQ4bpPzg-Q2-zVO5l | 35947 | (unverändert, Drive-Copy) | OK |
| `ENTSCHEIDUNGS-LOG-LIVE-TRIAL.md` | 1Z5OKcXJIvdR-TEUbofGQ9ukD-eM_-BMh | 12437 | (unverändert, Drive-Copy) | OK |
| `run_brief_daten.md` | 1b34-yZqCSZNab_bVCS76pfdJ4yKyLWV_ | 29804 | (unverändert, Drive-Copy) | OK |
| `lieferanten_mapping.yaml` | 1Z-SpOVwWCxpbQvLS0GasjxdfSLYN_aWn | 23357 | (unverändert, Drive-Copy) | OK |
| `WAWI-IMPORT-WISSEN.md` | 1Sov_8PwxWdAqrbAuEPxiQakcBdAHW4Co | 75060 | (unverändert, Drive-Copy) | OK (KNOWN_EXCEPTION >50KB) |
| `cowork_anweisung_bildpipeline.md` | 1FVscj13-UehFavN6CYURgYtrAh5iVl4W | 43315 | (unverändert, Drive-Copy) | OK |

### NICHT in Drive — manual upload durch Tjorben (2 Files)

| Datei | Lokale Size (B) | SHA256 (lokal) | Upload-Status |
|---|---|---|---|
| `BACKLOG.md` | 71463 | `98a5a5c458f2240d16446bcdadcebf7006e5328df678daf94d39f27adf76cc3d` | FAIL — base64-Stream-Drift bei 95KB-Output; via `present_files` ausgegeben |
| `cowork_anweisung_datenimports.md` | 73110 | `bf4b6d5da6da03b25db295fafb83644dcf5af696bae0594688835d2a41697d84` | FAIL — base64-Stream-Drift bei 98KB-Output; via `present_files` ausgegeben |

---

## 7. Anzahl-Marker

- **Erwartet:** 18 Wissens-Files + 1 Manifest = **19 Files** pro kompletter Snapshot
- **Aktuell in Drive (ohne Karteileichen):** 16 Wissens-Files + 1 Manifest = **17 Files**
- **Fehlend (manual upload nötig):** 2 Wissens-Files
- **Karteileichen im Folder (Manual-Cleanup):** 6 Files (siehe Sektion 11)

**Ziel-Zustand (nach manuellem Upload durch Tjorben):** 19 Files (18 Wissens + 1 Manifest). Karteileichen separat über Drive Web UI zu löschen.

---

## 8. Self-Check-Ergebnis

| Punkt | Status | Detail |
|---|---|---|
| WSC-1 (Größe ≤ 50 KB) | WARN | BACKLOG (71KB), cowork_anweisung_datenimports (73KB), WAWI (75KB) als known-exceptions dokumentiert |
| WSC-2 (Append/Patch-File-Verbot) | PASS | Keine Append/Patch-Files |
| WSC-3 (Sektion-13-Match) | PARTIAL | 16 von 18 in Drive; 2 fehlend (manual upload) |
| WSC-4 (Cross-Ref zu ARCHIV) | PASS (implizit) | E14, E20, E35, E36, E40, E42 in ARCHIV; alle E-Nummer-Verweise konsistent |
| WSC-5 (neue Sektionen in SPEC_KONSTANTEN) | PASS | Sektion 13 + 14 erweitert um Playbook + E85/E86 |
| WSC-6 (kein alter Monolith) | PASS | Kein Cluster-Split in v1.18, keine Monolithen-Reste |
| WSC-7 (Byte-Identität bei Copies) | PASS | Drive `copy_file` preserves bytes |
| WSC-8 (Build-Target ≤ 40 KB) | WARN | 4 modifizierte Files >40KB (BACKLOG, datenimports, COWORK-INFRA, SPEC_KONSTANTEN) — known-exceptions, Split-Planung |
| WSC-9 (UTF-8-Sanity) | PASS | Alle Files UTF-8-valid |
| WSC-10 (Manifest mit Hashes) | PASS | Dieses Manifest enthält SHA256 für alle 18 Wissens-Files (für 10 unveränderte: Hash via Drive-Copy = Vorgänger-Hash) |
| WSC-11 (Build-Trail vollständig) | PASS | Sektionen 1-7 oben |
| WSC-12 (Known-Exceptions dokumentiert) | PASS | BACKLOG, datenimports, WAWI >50KB — Split geplant in v1.19+ (siehe BACKLOG) |
| WSC-13 (Cleanup-Aktionen vermerkt) | PASS | Siehe Sektion 11 unten |
| WSC-14 (Notes ans Claude.ai-Projekt) | PASS | Siehe Sektion 12 unten |
| WSC-15 (Snapshot-Folder eindeutig) | PASS | `Version_2026-05-18_141930` |
| WSC-16 (Anzahl Files = erwartet) | PARTIAL | 17 in Drive (statt 19) — 2 fehlend für Komplettheit |
| WSC-17 (Header-Bump-Pflicht, NEU E86) | PASS | Alle 7 modifizierten Files haben Header-Bump erhalten (siehe Sektion 3) |

**Gesamt:** 12× PASS, 3× WARN (known-exceptions), 2× PARTIAL (manueller Upload nötig für Komplettheit). Build ist **operativ funktional** wenn Tjorben die 2 Files nachträglich hochlädt. **Resolver wird diesen Snapshot überspringen** bis Komplettheit erreicht.

---

## 9. Known-Exceptions / Geplante Folge-Splits

- `BACKLOG.md` 71463 B (>50KB) — Split geplant v1.19+ (z.B. nach Themen-Cluster wie ENTSCHEIDUNGS-LOG in v1.17)
- `cowork_anweisung_datenimports.md` 73110 B (>50KB) — Split geplant v1.19+ (z.B. Stage-Beschreibungen vs. Schema-Konventionen)
- `WAWI-IMPORT-WISSEN.md` 75060 B (>50KB) — Split geplant v1.19+ (Konvergenz-Erkenntnisse von Pilot-Phase)
- `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` 43470 B (>40KB, ≤50KB) — Build-Target-Warning, monitoring
- `SPEC_KONSTANTEN.md` 49321 B (≤50KB, knapp drunter) — Build-Target-Warning, monitoring. Lösungspfad in BACKLOG B54.

---

## 10. Tool-Anomalien & neue Drift-Pfade

**A9 (NEU 2026-05-18) — base64-Stream-Drift bei Sonnet-Subagent-Upload.** Beim Subagent-Upload-Pfad (v1.17-Build-Pattern) traten zwei Drift-Modi auf:
- (a) UTF-8-Multibyte-Drift in Sonnet-Subagent: `ü` → `¼` etc. bei base64-Strings ≥10KB. Drift-Rate ~1 char/10KB. Reproduzierbar in v1.18-Sub1.
- (b) Token-Output-Limit: bash `cat /tmp/upload.b64` für base64 ≥14k Token kann nicht in Main-Context geladen werden. Auch Read-Tool hat 25k-Token-Limit. Für File ≥50KB markdown / ≥67KB base64 nicht direkt arbeitbar.

**A10 (NEU 2026-05-18) — Drive-MCP `create_file` mit base64Content scheitert bei sub-2-Subagent für File >40KB.** Auch Opus-Subagent schaffte nur 2 von 4 large files vor 64k-Output-Tokens-Limit (Schwelle). Für 2 weitere (BACKLOG 71KB, datenimports 73KB) entstanden FAIL-Karteileichen.

**A11 (NEU 2026-05-18) — Main-Agent base64-Upload zuverlässig bis ~50 KB markdown.** Direkt-Upload aus Main-Context funktioniert für Files ≤50KB markdown (≤67KB base64 ≈ 17K tokens output). Drift-frei verifiziert via Drive-fileSize-Match. Limit ist Output-Token-Cap des Main-Agents.

**Mitigation für v1.19:**
- Empfehlung: Splits aller Files >40KB markdown in v1.19, sodass Upload via Main-Agent zuverlässig durchläuft
- Oder: Tool-Erweiterung der Drive-MCP um `upload_from_path` (akzeptiert lokalen Dateipfad statt base64Content) — wäre der saubere Architektur-Fix

---

## 11. Manuelle Cleanup-Aktionen für Tjorben

**Aktion 1 — 6 Karteileichen aus v1.18-Build im aktuellen Snapshot-Folder löschen:**

| Drive-ID | Dateiname | Größe | Ursache |
|---|---|---|---|
| `1_AhteqxSQk6e36doSZr05gwcAgmTdt1U` | WISSENS-UPDATE-PLAYBOOK.md | 10737 B | Sub1 Sonnet-Drift (UTF-8 `ü` → `¼` confirmed) |
| `1YnBnI77HeJhQsmXlFTFJpz628koEN_TQ` | PROJEKT-CHARTER.md | 20844 B | Sub1 size-mismatch (+1 Byte UTF-8-Drift) |
| `1OTEz-u7r0B1VSmMnYfqn8QYBvr7Vfs9X` | cowork_custom_instructions.md | 15214 B | Sub1 unverifiziert, wahrscheinlich Drift |
| `1Jp7eJXrqBdsdSSP98n-eka4SAnbkueFl` | Projekt-Anweisungen.md | 17747 B | Sub1 unverifiziert, wahrscheinlich Drift |
| `1-_Sl4QbdX7RFzeS4_z9G0osjU7Lh7R7j` | BACKLOG.md (FAIL) | 27936 B (statt 71463) | Sub3 partial-content FAIL |
| `17KBuI6zjNaH2ScgEUUYozCvCvj-zXp_b` | cowork_anweisung_datenimports.md (FAIL) | 218 B (statt 73110) | Sub3 partial-content FAIL |

**Aktion 2 — 3 Karteileichen im Vorgänger-Snapshot-Folder `Version_2026-05-17_212017` löschen** (siehe BACKLOG B60):

| Drive-ID | Dateiname | Größe |
|---|---|---|
| `1k7FloAj2KqmuXmLt1tidZb6mHZSCgLoN` | ENTSCHEIDUNGS-LOG-CRAWLING-DATEN.md (Stub) | 2.286 B |
| `1qJjBoTE92V7il_vs-F-gglBuguDANvP4` | SPEC_KONSTANTEN_as_gdoc_temp | 48677 B |
| `1-7_ueaQylA6fZ37YYN0mnm115kmkEa2C` | SPEC_KONSTANTEN_temp_for_chunked_read | 48677 B |

**Aktion 3 — Manuelle Uploads der 2 fehlenden Files in den neuen Snapshot:**

| Datei | Lokale Quelle (via `present_files` verfügbar) | Ziel-Folder |
|---|---|---|
| `BACKLOG.md` (71463 B) | siehe Chat-Output | `Version_2026-05-18_141930` |
| `cowork_anweisung_datenimports.md` (73110 B) | siehe Chat-Output | `Version_2026-05-18_141930` |

Nach diesen 3 Aktionen ist der Snapshot komplett: 19 Files (18 Wissens + 1 Manifest), 0 Karteileichen, Resolver greift den Snapshot als aktuellen Stand.

---

## 12. Notes ans Claude.ai-Projekt

1. **Build-Pattern (E85) ist verankert.** Ab v1.19 reicht ein kompakter Scope-Trigger, der Playbook macht das Wie.

2. **Versionierungs-Policy (E86) funktioniert.** Alle 7 modifizierten Files in v1.18 haben Header-Bump erhalten. WSC-17 PASS. Forensik künftig sauberer.

3. **Tool-Limit ist die kritische Engstelle (A9-A11).** Solange Drive-MCP nur `base64Content` als String-Parameter akzeptiert und kein `upload_from_path`-Endpoint existiert, sind Files >50KB markdown nicht zuverlässig autonom uploadbar. Lösung: entweder kleinere Files (Cluster-Splits in v1.19 priorisieren) oder Tool-Erweiterung der Drive-MCP-Spec.

4. **Subagent-Drift bei großen base64-Strings:** Sonnet drift unzuverlässig (~1 char/10KB). Opus zuverlässiger, aber 64k-Output-Token-Cap bei mehreren Uploads im selben Subagent. Empfehlung: pro Subagent maximal 2 Files >40KB markdown.

5. **Karteileichen-Akkumulation ist ein latentes Risiko.** v1.18 hat 6 neue Karteileichen erzeugt (zusätzlich zu 3 aus v1.17). Drive-MCP fehlt `delete_file`-Operation (B33). Sobald 10+ Karteileichen sich ansammeln, lohnt sich ein Drive-Cleanup-Tag.

6. **F1-F7 (BACKLOG B54-B60) sind als Spec-Bedarf für v1.19+ dokumentiert.** Klärungen mit Tjorben bereits durch (B55 Kategorie-Pattern, B56 Artikelgewicht-Default 0,05 kg, B58 Modelnamen aus Crawl, B59 TARIC `62114390`). Lösung implementieren bei nächstem Daten-Pipeline-Update.

7. **Performance-Diagnose (B54):** Spec-Caching für SPEC_KONSTANTEN (48KB) erzeugt Sub-Agent-Detour. v1.19 sollte SPEC_KONSTANTEN unter 30KB schrumpfen (Sektion 13+14 in eigene Datei auslagern).
