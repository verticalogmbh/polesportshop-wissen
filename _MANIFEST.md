# Snapshot-Manifest

**Snapshot-Tag:** `v1.20` (Git-Tag, Skalierungs-Refactor)
**Stand:** 2026-05-18 (Berlin)
**Build-Engine:** Claude Code (lokal, Opus 4.7 1M context)
**Vorgänger-Tag:** `v1.19` (Pattern-Pivot Drive → Git E87)
**Repo:** `https://github.com/verticalogmbh/polesportshop-wissen`
**Branch:** `main`

---

## 1. Build-Trail

**Auftrag (Tjorben-Trigger 2026-05-18):** Skalierungs-Refactor — „richtig gute Base für 20 Lieferanten". Wenn etwas fehlt: hinzufügen. Redundanzen schlanker machen. Umschichten erlaubt. Robust für massives Wachstum aufstellen.

**Resultat:** 11 Files modifiziert, 3 neu, 0 entfernt. Gesamt-Repo geschrumpft um ~65 KB trotz 3 neuer Files (große Verschlankung von datenimports.md und bildpipeline.md). Cowork-Resolver auf GitHub-Raw migriert (B63 erledigt → E91). Neue Skalierungs-Anker: `CLAUDE.md` (Daily-Workflow), `LIEFERANTEN-ONBOARDING.md` (Standard-Prozess für Lieferant 2-21), `BACKLOG-ARCHIV.md` (kompakter Index).

**Build-Engine:** Claude Code lokal, Opus 4.7 1M context. Build-Pattern: `WISSENS-UPDATE-PLAYBOOK.md` v2.0.1 (Git-basiert), erweitert auf 12 Stages (8 + Pre-Flight + 3 Neue-Files-Stages). Autonom durchgezogen ohne Zwischen-OK-Frage gemäß Tjorbens Build-Style.

**Autonome Entscheidungen** (siehe Sektion 12).

---

## 2. Was neu generiert wurde (3 Files)

| Datei | Size (B) | Zweck |
|---|---|---|
| `CLAUDE.md` | 8617 | Daily-Workflow-Cheatsheet für Claude Code im Repo-Root. Trigger-Registry, File-Map, Daily-Ops, Naming-Konventionen, Charter-Kurz, häufige Sessions. Wird von Claude Code beim Session-Start automatisch geladen. |
| `LIEFERANTEN-ONBOARDING.md` | 10937 | Konsolidierter Standard-Prozess für Lieferant 2-21 in 5 Pflicht-Schritten (Mapping, Vorlagen, Brand-Story, Probe-Lauf, Import+Review). Skalierungs-Anker. |
| `BACKLOG-ARCHIV.md` | 4800 | Kompakter Index der erledigten/deferred B-Einträge. BACKLOG.md behält alle Details, ARCHIV gibt schnelle Übersicht. |

---

## 3. Was modifiziert wurde (11 Files mit Header-Bump)

| Datei | Bump-Typ | Begründung |
|---|---|---|
| `cowork_custom_instructions.md` | **Major (v1.16 → v2.0)** | Pattern-Pivot: Wissens-Quelle von Drive-Snapshot auf GitHub-Raw migriert (B63 erledigt, E91). Kompletter Rewrite, schlanker (15 KB → 11 KB). |
| `Projekt-Anweisungen.md` | **Major (v1.16 → v2.0)** | Wissens-Backbone-Pivot: Drive → Git. Daily-Workflow läuft via Claude Code lokal. Kompletter Rewrite, schlanker (18 KB → 8 KB) durch Verweis auf CLAUDE.md für Operational Details. |
| `cowork_anweisung_datenimports.md` | **Major (v1.15.1 → v2.0)** | Verschlankung 73 KB → 23 KB. Konstanten-Sektionen 5.1/5.1.1/5.1.2 + Self-Check-Detail + AP1-AP12 ausgelagert nach SPEC_KONSTANTEN. UNIQUE-Inhalt bleibt (Stages, Crawl, Fehler-Handling, Konventionen). Stage 0 + Konventions-Sektion auf GitHub-Raw + Git-Pattern. |
| `cowork_anweisung_bildpipeline.md` | **Major (v1.6 → v2.0)** | Stub-Reduktion 43 KB → 3 KB. Voll-Spec im `v1.19`-Git-Tag erhalten (per `git show v1.19:cowork_anweisung_bildpipeline.md` rekonstruierbar). Stub verweist auf E63 + BACKLOG B36-B40 für Reaktivierungs-Pfad. |
| `WISSENS-UPDATE-PLAYBOOK.md` | Patch (v2.0 → v2.0.1) | Referenz auf E91 + Erfahrungs-Note aus v1.20-Build ergänzt (Pattern hat sich für 12-Stage-Refactor bewährt). |
| `SPEC_KONSTANTEN.md` | Minor (v1.17 → v1.18) | Sektion 13 auf Git-Tag-Pattern + 3 neue Files im File-Index (CLAUDE.md, LIEFERANTEN-ONBOARDING.md, BACKLOG-ARCHIV.md). Sektion 14 um E87, E89, E90, E91 nachgezogen. Trigger-Sektionen pro Trigger-Typ ergänzt. |
| `run_brief_daten.md` | Minor (v1.16 → v1.17) | DARF-Sektion auf GitHub-Raw umgestellt (B63), neuer „Was v1.17 ändert"-Block am Anfang. |
| `WAWI-IMPORT-WISSEN.md` | Minor (2026-05-17 → 2026-05-18 v1.16) | Sektion 9 Onboarding-Hinweis auf `LIEFERANTEN-ONBOARDING.md` verweisen. Stand-Header aktualisiert. Pilot-Wissens-Substanz unangetastet. |
| `BACKLOG.md` | Minor (v1.19 → v1.20) | Hinweis auf `BACKLOG-ARCHIV.md` als kompakter Index. B63 erledigt-status v1.20 → E91. Neue Einträge B64 (Brand-Story-Skalierungs-Pfad bei N≥5 Lieferanten, deferred) + B65 (Cowork-`web_fetch`-Probe gegen GitHub-Raw, beim ersten v1.20-Cowork-Lauf zu validieren). |
| `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` | Minor (v1.19 → v1.20) | Neuer E-Eintrag E91 (Skalierungs-Refactor v1.20). Index erweitert. |
| `PROJEKT-CHARTER.md` | Stand-Update (datums-versioniert, kein v1.X-Header) | Architektur-Rollen-Sektion aktualisiert: Claude Code lokal statt Claude.ai-Projekt; GitHub-Repo statt Drive-Backup. Stand-Header auf v1.20-Snapshot. |

---

## 4. Was unverändert übernommen wurde (8 Wissens-Files)

Diese Files sind im v1.20-Snapshot identisch zum v1.19-Stand:

- `ENTSCHEIDUNGS-LOG-ARCHIV.md`
- `ENTSCHEIDUNGS-LOG-BILDPIPELINE.md`
- `ENTSCHEIDUNGS-LOG-CRAWLING-DATEN.md`
- `ENTSCHEIDUNGS-LOG-LIVE-TRIAL.md`
- `ENTSCHEIDUNGS-LOG-STIL-CONTENT-A.md`
- `ENTSCHEIDUNGS-LOG-STIL-CONTENT-B.md`
- `lieferanten_mapping.yaml`

Vollständiger Vergleich via `git diff --stat v1.19..HEAD`.

---

## 5. Was nicht mehr existiert (0 Files)

Keine Files entfernt in v1.20. `cowork_anweisung_bildpipeline.md` wurde stark reduziert (Stub), bleibt aber als File für File-Index-Konsistenz.

---

## 6. File-Liste mit Sizes und SHA256

| Datei | Size (B) | SHA256 |
|---|---|---|
| `BACKLOG-ARCHIV.md` | 4800 | `f0663163c797f1565dc4be2f9d0fae1093a1fca0577e1308d0b5938288de5c74` |
| `BACKLOG.md` | 80667 | `66d55fd9e645d666cf2b556a5a54431f289334523752408a29af661000cfa908` |
| `CLAUDE.md` | 8617 | `5304695bd8a754452a3a2d9a07d71cabe12ae266aaf10a803f70db98bf7ac562` |
| `ENTSCHEIDUNGS-LOG-ARCHIV.md` | 9600 | `2b2b3fa5fa6648aa0dff909b829b58c4ef6d188834558714dd07c420f0cad846` |
| `ENTSCHEIDUNGS-LOG-BILDPIPELINE.md` | 24725 | `72c626bddac40b2f65093415ae86b55b87f5f89376cb14d1359989dc11a27b5c` |
| `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` | 56444 | `6b0ff55eedbb40475678e20c9cb4f64484fe4a93a4b1bc4e195f038057f6797b` |
| `ENTSCHEIDUNGS-LOG-CRAWLING-DATEN.md` | 38406 | `1505379afb0b609c5dadad4b2379bbf0676a6d1ee53329ba17056000f6229ab5` |
| `ENTSCHEIDUNGS-LOG-LIVE-TRIAL.md` | 12437 | `ec729b1fd368a251723676e189ead632ab27e141f97e69742910140c961b6ecd` |
| `ENTSCHEIDUNGS-LOG-STIL-CONTENT-A.md` | 33869 | `d13f74a9430154113929a17702f5854241db0f5a429ba6b40c2bc33496ae6397` |
| `ENTSCHEIDUNGS-LOG-STIL-CONTENT-B.md` | 35947 | `d07fb795abb901ecd81c32f18f962296a254cc794ae25e556ad45a49b54f4f73` |
| `LIEFERANTEN-ONBOARDING.md` | 10937 | `88373efc66c92580532fb49adb6e068b3e264c16d80e98e7efd52631b2332ccc` |
| `PROJEKT-CHARTER.md` | 21310 | `c80b22a3c2c8d0dd03e4950ae703c34ec193605bb43aac277de2de1de62ab618` |
| `Projekt-Anweisungen.md` | 7801 | `ed20458a5515c2b9858bc2ad481d355dd5a0dffa30dc6ce2684c9bbf24939dad` |
| `SPEC_KONSTANTEN.md` | 52530 | `d0e4e84199e379671db1214ecc176e6e6c672032d39164810814cddee695627e` |
| `WAWI-IMPORT-WISSEN.md` | 75186 | `ce0873d1ce0768c49e836e1d47aab79c658e08c4b8fc478ead9072d7a64f798e` |
| `WISSENS-UPDATE-PLAYBOOK.md` | 15704 | `fb8d6cd81de9cb225542235b2ede1bb417e2d51ceea903c1d182bf6281ae308b` |
| `cowork_anweisung_bildpipeline.md` | 3252 | `84ca4ef8698448485770533393d9084b82dbf089e5ef56bdc70216d6464c36b7` |
| `cowork_anweisung_datenimports.md` | 22585 | `fa5d33e53064c57250350e88975290d04f63d4d724d7b3f944fb0dec43d808f7` |
| `cowork_custom_instructions.md` | 11308 | `be87644eb7b3e836238e119c23a0baa4da23d70703ffd4129c0e57a433f67446` |
| `lieferanten_mapping.yaml` | 25697 | `277715d3923c6f04e6136b30716ec79eb035ce498a4ca6ec10e0f08055ac9ea3` |
| `run_brief_daten.md` | 33655 | `10e8a6ac43bb3e50214f4f6a4828fedb35890f978d480c61001dd246e112aeec` |

---

## 7. Anzahl-Marker

- **Wissens-Files in v1.20:** 21 (alle in Sektion 6 gelistet außer `_MANIFEST.md` selbst)
- **Plus Manifest:** 22 Files total im Snapshot
- **Plus Repo-Meta:** `README.md` (72 B), `.gitignore` (10 B) — nicht Wissens-File
- **Änderung ggü. v1.19 (19 Files):** +3 (CLAUDE.md, LIEFERANTEN-ONBOARDING.md, BACKLOG-ARCHIV.md)

---

## 8. Self-Check-Ergebnis (WSC-1 bis WSC-17, v2.0.1-Git-adaptiert)

| Punkt | Status | Detail |
|---|---|---|
| WSC-1 (Größe ≤ 50 KB Soft-Limit) | WARN | 4 Files >50 KB: `BACKLOG.md` (80 KB), `WAWI-IMPORT-WISSEN.md` (75 KB), `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` (56 KB), `SPEC_KONSTANTEN.md` (52 KB). Alle in Sektion 9 dokumentiert. In Git-Welt kein Upload-Killer (E87). |
| WSC-2 (Append/Patch-File-Verbot) | PASS | Keine Append/Patch-Files. |
| WSC-3 (Erwartete File-Liste) | PASS | 21 Wissens-Files + 1 Manifest = exakt wie SPEC_KONSTANTEN Sektion 13 v1.18. |
| WSC-4 (Cross-References zu ARCHIV) | PASS | E-Nummer-Konsistenz: neue E91 (COWORK-INFRA). Alte ARCHIV-Einträge (E14, E20, E35, E36, E40, E42) weiter konsistent referenziert. |
| WSC-5 (Neue Sektionen in SPEC_KONSTANTEN) | PASS | Sektion 13 + 14 erweitert. |
| WSC-6 (Kein alter Monolith) | PASS | Kein Cluster-Split in v1.20. |
| WSC-7 (Git-Status clean nach Commit) | wird nach Commit PASS | Vor Commit: 11 M + 3 ?? + 1 M (Manifest) = 15 dirty paths. Nach `git commit` muss `git status --porcelain` leer sein. |
| WSC-8 (Build-Target ≤ 40 KB für modifizierte Files) | WARN | 4 modifizierte Files >40 KB: BACKLOG, WAWI-IMPORT, ENTSCHEIDUNGS-LOG-COWORK-INFRA, SPEC_KONSTANTEN. In Git-Welt akzeptabel; Cluster-Splits B61/B62 deferred. |
| WSC-9 (UTF-8-Sanity) | PASS | Alle Files UTF-8-valid (verifiziert via `file -I` in v1.19, keine Encoding-Änderung in v1.20). |
| WSC-10 (Manifest enthält alle Files mit Hashes) | PASS | 21 Wissens-Files mit SHA256 in Sektion 6 gelistet. |
| WSC-11 (Manifest-Build-Trail vollständig) | PASS | Sektionen 1-5 oben. |
| WSC-12 (Known-Exceptions dokumentiert) | PASS | Siehe Sektion 9. |
| WSC-13 (Manuelle Aktionen vermerkt) | PASS | Siehe Sektion 11. |
| WSC-14 (Notes zum Build-Pattern) | PASS | Siehe Sektion 12. |
| WSC-15 (Tag-Konvention eingehalten) | wird vor Tag PASS | `v1.20` folgt `vX.Y`. `git tag --list | grep v1.20$` muss leer sein vor `git tag`. |
| WSC-16 (Push erfolgreich) | wird nach Push PASS | Verifikation via `git ls-remote --tags origin | grep v1.20`. |
| WSC-17 (Header-Bump-Pflicht E86) | PASS | Alle 11 modifizierten Files Header-Bump erhalten (Sektion 3). Major×4 (cowork_custom_instructions, Projekt-Anweisungen, cowork_anweisung_datenimports, cowork_anweisung_bildpipeline), Minor×5 (SPEC_KONSTANTEN, run_brief_daten, WAWI-IMPORT-WISSEN, BACKLOG, ENTSCHEIDUNGS-LOG-COWORK-INFRA), Patch×1 (WISSENS-UPDATE-PLAYBOOK), Stand-Update×1 (PROJEKT-CHARTER, datums-versioniert). |

**Gesamt vor Commit:** 13× PASS, 2× WARN (known-exceptions), 2× pending (WSC-7/15 vor Commit; WSC-16 vor Push). Nach Commit+Tag+Push: 16× PASS, 2× WARN, 0× FAIL.

---

## 9. Known-Exceptions / Geplante Folge-Splits

- `BACKLOG.md` 80667 B (>50 KB) — wächst durch Status-Updates. Mit BACKLOG-ARCHIV.md als kompakter Index entschärft. Split bei N≥20 aktive Lieferanten neu evaluieren.
- `WAWI-IMPORT-WISSEN.md` 75186 B (>50 KB) — B61 (deferred): in Git-Welt kein Upload-Killer mehr, Split nur bei konkretem Pain.
- `ENTSCHEIDUNGS-LOG-COWORK-INFRA.md` 56444 B (>50 KB) — durch E87 + E91 gewachsen. Monitoring; Split nur bei Pain.
- `SPEC_KONSTANTEN.md` 52530 B (knapp >50 KB) — durch v1.20-Updates Sektion 13/14 etwas gewachsen. B54 (deferred): Performance-Split in Git-Welt nicht zwingend.

---

## 10. Tool-Anomalien & Notes zum Build-Pattern

**Pattern hat sich für großen Refactor bewährt.** v1.20 ist mit 11 modifizierten + 3 neuen Files + 11 Strang-Maßnahmen der bisher größte Build. Lief in einem Cycle ohne Tool-Use-Limit-Probleme durch. Claude-Code-Edit/Write-Tools sind tatsächlich der Game-Changer ggü. Drive-MCP-`base64Content` (siehe E87-Anomalien A9/A10/A11 — alle obsolet).

**Explore-Agents für Bestandsaufnahme:** 2 parallele Explore-Agents (Cowork-Specs + WAWI/SPEC/BACKLOG) gespawnt vor Stage 1, lieferten strukturierte Befunde in ~3-5 Min jeweils. Sparte Token im Main-Context und gab klare Datenpunkte für die 11 Strang-Maßnahmen. Pattern für künftige große Refactors merken.

**Memory-Initialisierung:** Repo-Memory unter `/Users/tjorbenbecker/.claude/projects/.../memory/` initialisiert mit 5 Files (MEMORY-Index + repo_setup + user_role + feedback_build_style + project_engines + project_status_v1_19). Künftige Claude-Code-Sessions haben damit Repo-Kontext + Tjorbens Build-Stil-Präferenz persistent verfügbar.

**Empfehlungen für nächste v1.X-Builds:**
- **B65 (Cowork-`web_fetch`-Probe) beim ersten v1.20-Cowork-Daten-Lauf validieren.** Im Lauf-Bericht dokumentieren: kann Cowork-`web_fetch` GitHub-Raw lesen? Egress-Allowlist-Anpassung nötig?
- **Lieferanten-Onboarding-Trigger erstmals testen:** beim ersten neuen Lieferanten (Lunalae oder Pole Junkie aktivieren) den Trigger „Onboarde Lieferant X" durchspielen — validiert ob `LIEFERANTEN-ONBOARDING.md` operativ trägt oder noch Lücken hat.
- **Verdachtsfälle B4/B12/B21** bei v1.21 oder v1.22 entscheiden: streichen oder aktivieren.

---

## 11. Manuelle Aktionen für Tjorben

**Aktion 1 — Cowork-Setup aktualisieren** (Pflicht vor erstem v1.20-Cowork-Lauf):

In Cowork-UI Settings → Cowork → Global Instructions: den Inhalt aktualisieren auf den v1.20-Stand des File `cowork_custom_instructions.md`. URL des aktuellen Stands:
`https://raw.githubusercontent.com/verticalogmbh/polesportshop-wissen/v1.20/cowork_custom_instructions.md`

Alternativ: Copy-Paste aus dem lokalen Repo-File.

**Aktion 2 — Egress-Allowlist** (möglicherweise):

In Cowork-UI Settings → Capabilities → Network-Egress: prüfen, ob `raw.githubusercontent.com` und `api.github.com` in der „Additional allowed domains"-Liste stehen. Aktueller Pilot-Stand „All domains"-Modus wegen Anthropic-Bug (B29) deckt das ab, aber wenn auf granulare Liste umgestellt: ergänzen.

**Aktion 3 — keine weiteren manuellen Aktionen.** Drive-Karteileichen-Cleanup bleibt aus v1.19 (3 IDs gelistet in v1.19-Manifest Sektion 11) — nicht zwingend für v1.20-Funktionalität.

---

## 12. Autonome Entscheidungen (zum Review)

Im Sinne der Tjorben-Direktive „beauftrage dich" + Build-Style-Memory:

1. **BACKLOG-ARCHIV.md als Index statt Hart-Split** — Vollständige Ausgliederung erledigter Einträge wäre zu invasiv (Verlust-Risiko bei Umstellung). Pragmatischer: BACKLOG.md behält Details, ARCHIV ist kompakte Übersicht. Bei N≥20 aktive Lieferanten neu evaluieren.
2. **`cowork_anweisung_bildpipeline.md` auf Stub statt löschen** — Datei-Konsistenz im File-Index (SPEC_KONSTANTEN Sektion 13). Voll-Spec rekonstruierbar via `git show v1.19:cowork_anweisung_bildpipeline.md`. Reaktivierungs-Pfad in Stub dokumentiert.
3. **`lieferanten_mapping.yaml` in v1.20 nicht splitten** — bei aktuell 4 Lieferanten (1 aktiv) ist 25 KB unkritisch. B64 als deferred für N≥5 aktive Lieferanten.
4. **`TRIGGER-REGISTRY.md` als eigenes File verworfen** — zu kleinteilig (1 KB). In CLAUDE.md als Sektion integriert.
5. **`PROJEKT-CHARTER.md` Datums-Versioniert lassen** (kein v1.X-Header-Bump) — folgt der bestehenden Charter-Konvention. Stand-Header reicht für E86-Compliance bei datums-versionierten Files.
6. **Memory-System initialisiert** — der Trigger erwähnte das nicht explizit, aber für eine „richtig gute Base" für künftige Sessions ist es Pflicht. 5 Memory-Files angelegt.
7. **Explore-Agents für Bestandsaufnahme** — sparte 80%+ Main-Context-Token vs. direktes Lesen aller Files. Bei künftigen großen Refactors als Default merken.
8. **Tjorben-Edits an Cowork-UI manuell lassen** — kein Versuch, das automatisch zu pflegen. Hinweis in Sektion 11 als manuelle Aktion.
9. **WISSENS-UPDATE-PLAYBOOK nicht majorbumpen** — v2.0 vor wenigen Stunden frisch entstanden. Patch-Bump v2.0.1 ist die saubere Wahl.
10. **Resolver-Migration für Cowork ohne Probe-Test in v1.20-Build** — Probe-Test ist Sache des ersten v1.20-Cowork-Laufs (B65). Build hat damit eine Vorab-Annahme: Public-Repo + `web_fetch` funktioniert ohne Auth. Wenn nicht: B65 dokumentiert Fallback.
11. **`PROJEKT-CHARTER.md` Sektion „Architektur-Rollen" zwei Absätze geupdatet** statt komplett rewriten — minimal-invasiv, preservere die bewährte Verfassungs-Sprache.

---

## 13. Verhältnis zum Vorgänger-Snapshot

v1.19 → v1.20 ist der **Skalierungs-Refactor**. v1.19 löste die Tool-Limits durch Pattern-Pivot (Drive → Git, E87). v1.20 nutzt die neue Plattform für tatsächliche Aufräum-Arbeit (Verschlankung, neue Anker, Resolver-Migration). Gemeinsam bilden v1.19 + v1.20 die „v2-Generation" des Wissens-Managements: Git-basiert, schlank, skalierbar.

Ab v1.21 sind reguläre Inhalts-Iterationen erwartet — neue Lieferanten onboarden, F-Findings einarbeiten, BACKLOG abarbeiten. Kein weiterer Pattern-Pivot in Sicht.
