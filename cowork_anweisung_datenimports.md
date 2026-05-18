# Cowork-Anweisung: Daten-Pipeline polesports

**Version:** v1.15.1 (Stand 2026-05-18, Patch: Performance-Diagnose-Hinweis in Sektion 3.1 + Cross-Verweis-Update gemäß E86). · **Vorheriger Stand:** v1.15, 2026-05-17.
**Änderungen ggü. v1.14 (= interne v1.9):**
- **Autonomie-Hoheit E81 (NEU v1.15) in Sektion 4 und 12:** Cowork entscheidet Workflow-Details (Batch-Splitting, Token-Budget-Reservierung, Stage-Reihenfolge) eigenständig. STOPP nur bei: fehlende Pflicht-Daten, unbekannte Sprach-Begriffe außerhalb Lookup, Goldstandard-Abweichungen, Mapping-null-Pflichtfelder, Drift-Verdacht. Im Lauf-Bericht autonome Entscheidungen explizit dokumentieren.
- **Stil-Verschärfung E82 (NEU v1.15) in Sektion 5.5:** Em-Dash bleibt verboten (E22). NEU verboten: Doppelpunkt im Fließtext UND in `<h2>`-Taglines, Meta-Einleitungs-Sätze („Die Maße:", „Die Pflege:"). Self-Check 13 prüft das.
- **Pre-Run Scope-Analyse Stage 0.5 (NEU v1.15, E83):** Cowork schätzt vor Stage 1 das Token-/Wallclock-Volumen, splittet bei Überschreitung autonom in Batches und dokumentiert die Aufteilung im Bericht.
- **Familien-erhaltende Split-Regel E84 (NEU v1.15) in Stage 0.5 und 5.8:** Outfit-Pair-Familien werden NIE über Batches gesplittet. Cross-Selling-Stage läuft im LETZTEN Batch und sieht alle vorherigen Batches als gemeinsamen Scope.
- **Cross-Selling-Kinder-Replikation E80-Erweiterung (v1.15) in Stage 5.8:** linke Spalte (`Artikelnummer`) listet Vater + alle Kind-IDs, rechte Spalte (`Artikelnummer Cross-Seller`) strikt Vater. Plus Modell-Stamm-Schlüssel mit Farbe `(modell_basis, farbe_im_namen)`. Plus Family-Refresh als optionaler Trigger-Modus.
- **Output-Konvention verschärft (Sektion 7):** AP10 (kein Drive-Upload für CSVs), AP11 (Datei-Naming `<NR>_<Typ>_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv` Pflicht), AP12 (keine leeren CSVs; bei Stage 5.8 ohne Beziehungen Datei weglassen und im Bericht vermerken). Bug-Beleg Live-Trial Batch 1 (2026-05-17): 3 korrupte AP10-Verstoß-Uploads in Drive — siehe BACKLOG B51.
- **Self-Check 15+16 in SPEC_KONSTANTEN.md neu formuliert** für Kinder-Replikation und Standardlieferant-Setting in Vorlagen. Cowork prüft das pro Lauf.
- **Standardlieferant-Pflicht in Vorlagen (NEU v1.15) in Sektion 6:** in jeder der 5 Ameise-Vorlagen muss Standardlieferant explizit gesetzt sein. Bug-Beleg: Live-Trial Batch 1 Attribute-Import 2026-05-17 mit 220 Warnungen wegen `_4_Attribute`-Vorlage mit Standardlieferant „nicht gewählt".

**Änderungen ggü. v1.8 (= interne v1.8, Übernahme aus v1.13):**
- **Konstanten-Auslagerung in SPEC_KONSTANTEN.md (E61, Charter-Prinzip 11):** Alle harten Konstanten (48-Spalten-Schema, SEO-Templates, Sprach-Lookup-Tabellen, Merkmalwerte, Kategorien, Self-Check 12-Punkte, AP1-AP8) sind in die neue Datei `SPEC_KONSTANTEN.md` ausgelagert. Sektionen 5.1, 5.1.1, 5.1.2, 5.3, Stage-6-Self-Check verweisen jetzt nur noch dort hin. Grund: in mehreren End-to-End-Versuchen verbrauchte Cowork ~50K Tokens beim Extrahieren dieser Konstanten aus den großen Spec-Dateien und kam nie hinter Stage 0.
- **Spec-Caching-Konvention (E62, NEU Sektion 3.1):** Wissens-Files werden einmalig zu Lauf-Beginn geladen, lokal im Workspace gecacht, **niemals pro Stage neu aus Drive geholt**. Spart Token-Volumen und Latenz dramatisch.
- **Bildpipeline archiviert (E63):** `cowork_anweisung_bildpipeline.md` ist nicht mehr aktiv. Tjorben pflegt Bilder bis auf Weiteres manuell in WaWi. Die 10 Bild-Spalten bleiben im Stammdaten-Schema verpflichtend, aber **standardmäßig leer**. Stage 5.6 (Bildpipeline-Aufruf) und Stage 5.7 (Bild-URL-Duplizierung) sind in dieser Version **deaktiviert**. Bilder-Architektur-Refactor in BACKLOG für späteren Zeitpunkt.

**Änderungen ggü. v1.7 (Übernahme aus v1.8):**
- **Schema-Reverse-Engineering v3.1 (E54):** Spalten-Reihenfolge folgt der ALT-Reihenfolge der HotCakes-Vorlage aus v2-Ära plus 10 Bild-Spalten am Ende. Lieferantenblock auf Position 36-38. Append-only-Konvention für Schema-Bumps.
- **A6-Pivot: CSVs nur lokal (E52):** Drive-Upload für CSVs entfällt komplett. Lauf-Bericht und Mapping-Cheatsheet gehen weiter nach Drive.
- **Mapping-Cheatsheet pro Lauf:** kleine Markdown-Datei mit Mapping-Tabelle plus operativen Settings.
- **WaWi-Merkmalwerte (E50):** statische Listen (Farbe Kleidung 15, Style Tops 11, Style Shorts 11), nur Deutsch in der CSV, zweistufige Farb-Logik.
- **Kategoriebaum-Mapping (E51):** „Pole Dance Kleidung" immer Ebene 1, passende Unterkategorie Ebene 2.
- **Stil-Briefing für Artikeldetails (E53):** polesportshop-Identität + Pole-Junkie-Reduktion = eigene Stimme.

**Änderungen ggü. v1.6 (Übernahme aus v1.7):**
- **Crawl-Modus B aktiv (E48):** Code-Execution + Browser-UA + Shopify-Storefront-JSON für Shopify-Lieferanten.
- **Pole-Junkie-Freigabe (E49):** Owner-Direktive ohne ToS-Vorbehalt.
- **`crawl_mechanik`-Feld im Lieferanten-Mapping.**

**Änderungen ggü. v1.5 (Übernahme aus v1.6):**
- **Snapshot-Resolution-Strategie (E47)** in Stage „Lieferantenkontext laden" eingebaut.

**Änderungen ggü. v1.4 (Übernahme aus v1.5):**
- **Pipeline erweitert auf 5 CSVs ab v1.14** (E46 + E80) — 4 Artikel-CSVs + 1 Cross-Selling-CSV.
- **Stammdaten-Schema v3 mit 48 Spalten** (E46 erweitert E36) — in v1.8 als v3.1 reverse-engineered (E54).
- **Plattform-Aktivierung der Bilder automatisch** (B5-Lösung über E46) — gilt weiter, sobald Bildpipeline reaktiviert wird.

Operative Anweisung für die automatisierte Generierung der Ameise-Daten-Import-CSVs aus Lieferanten-Eingabematerial.

> **Konstanten-Quelle:** `SPEC_KONSTANTEN.md` ist die **kanonische** Quelle für alle harten Konstanten dieser Pipeline (Schema, Templates, Lookup-Tabellen, Self-Check, Anti-Patterns). Diese Anweisung beschreibt das *Was und Warum*; SPEC_KONSTANTEN.md beschreibt das *Genau-Wie*.

> **Schwester-Dokument:** `cowork_anweisung_bildpipeline.md` (v1.6, **ARCHIVIERT mit E63**) — nicht aktiv ausgeführt, Wissens-Referenz für späteren Architektur-Refactor.

> **Operatives Pilot-Wissen:** `WAWI-IMPORT-WISSEN.md` ist die hart erkämpfte Pilot-Spiegelung dieser Anweisung. Bei Konflikt: WAWI-IMPORT-WISSEN gewinnt im operativen *Wie*, diese Anweisung beschreibt das *Was und Warum*. SPEC_KONSTANTEN.md ist kanonisch für Konstanten.

> **Autonomie-Hoheit (E81, NEU v1.15):** In dieser Anweisung definierte Stages, Algorithmen und Konventionen sind verbindlich. **Wie** Cowork sie operativ umsetzt (Batch-Größe, Token-Reservierung, parallele Stages wo unkritisch), entscheidet Cowork autonom. STOPP-Trigger sind in Sektion 4 und 12 explizit aufgelistet — alles andere wird ohne Nachfrage durchgeführt und im Lauf-Bericht dokumentiert.

---

## 1. Zweck

Cowork verarbeitet Lieferanten-Input und erzeugt **5 CSVs** pro Lauf (ab v1.14, E80):

1. `1_Stammdaten_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv` — Artikel-Vater + Größen-Kinder, inkl. Lieferantenblock-Spalten **und 10 Bild-URL-Spalten** (`Bild 1` bis `Bild 10`)
2. `2_Variationen_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv` — Größen-Varianten in 5 Sprachen
3. `3_Merkmale_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv` — Strukturierte Filter (auf Vater UND Kind, E19/E34)
4. `4_Attribute_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv` — Reichtext-Inhalte (auf Vater UND Kind, E34)
5. `5_CrossSelling_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv` — **NEU v1.14, E80, mit Kinder-Replikation v1.15** — Cross-Selling-Beziehungen, 3 Spalten: `Artikelnummer; Artikelnummer Cross-Seller; Cross-Selling-Gruppe`. Eigener Ameise-Import-Typ „Cross-Selling-Artikel".

**Datei-Naming-Konvention (AP11, Pflicht v1.15):** Pattern `<NR>_<Typ>_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv`. NR ist 1-5, Typ ist `Stammdaten`/`Variationen`/`Merkmale`/`Attribute`/`CrossSelling` (CamelCase ohne Bindestrich). LIEFERANT ist `kuerzel` aus Mapping in UPPERCASE. Bug-Beleg Live-Trial Batch 1 (2026-05-17): Cowork hatte mehrere Files ohne NR-Präfix geschrieben („Stammdaten_HotCakes_..." statt „1_Stammdaten_HOTCAKES_..."), was Ameise-Reihenfolge-Setup erschwerte. AP11 fixiert das.

> **Historische Hinweise:**
> - Bis v1.2 gab es zusätzlich eine separate `Lieferantendaten`-CSV — abgeschafft mit E35, die Felder leben jetzt direkt in der Stammdaten-CSV. Bestehende HotCakes-Vorlage `_3_Lieferantendaten` in WaWi bleibt als Legacy ohne Funktion.
> - Bis v1.4 gab es zusätzlich eine separate `5_Bilder`-CSV mit Import-Typ *Artikelbilder pro Plattform* — abgeschafft mit E46 (2026-05-15), die Bild-URLs leben jetzt als Spalten `Bild 1` bis `Bild 10` direkt in der Stammdaten-CSV. Plattform-Aktivierung läuft automatisch über die Stammdaten-Vorlage mit konfigurierten Häkchen im Reiter „Bilder/Plattformen". Bestehende HotCakes-Vorlage `_5_Bilder` bleibt als Legacy in WaWi ohne Funktion.

---

## 2. Trigger & Input-Modi

### 2.1 Trigger

Manuelle Auslösung durch den Einkäufer im Chat. Kein Auto-Trigger, kein Polling.

> "Verarbeite neue Artikel von `<Lieferant>`, hier `<Input>`: `<Daten/Pfad/URL>`"

### 2.2 Input-Modi

| Modus | Erkennungssignal | Verarbeitung | Status Pilot |
|---|---|---|---|
| **firecrawl-Crawl** | URLs zu Lieferanten-Shop | firecrawl-MCP, LLM-Extract pro Produktseite | **Nicht aktiv** (E41/B25 — Firecrawl nicht in Cowork-Registry) |
| **Drive-Link** | Drive-URL | Drive-Tools, Inhalt einlesen | Aktiv |
| **Excel/CSV-Upload** | `.xlsx`, `.xls`, `.csv` | Datei parsen, Zeilen als Artikel | Aktiv |
| **PDF-Upload** | `.pdf` | LLM-basiert extrahieren | Aktiv |
| **Mail-Inhalt** | Text mit Lieferanten-Kontext | LLM-strukturiert parsen | Aktiv |
| **shopify_json** | Hersteller-URL mit Shopify-Fingerprint | Code-Execution + Browser-UA gegen Storefront-JSON (E48) | Aktiv |
| **Hybrid** | Kombination | Alle Quellen parallel, am Ende konsolidieren | Aktiv |

Cowork erkennt den Modus durch direkte Hinweise, Datei-/URL-Form, bei Mehrdeutigkeit kurze Nachfrage.

### 2.3 Trigger-Beispiele

```
"Verarbeite neue Artikel von POLE ADDICT, hier der Drive-Link: https://drive.google.com/..."
"Verarbeite neue Artikel von HotCakes Polewear, Excel anbei"
"Verarbeite neue Artikel von Bad Kitty, PDF anbei"  [PDF im Chat-Anhang]
"Verarbeite neue Artikel von Super Fly Honey, hier die Mail vom Lieferanten: [Text]"
"Verarbeite neue Artikel von Lunalae, hier ist ein Hybrid-Input: Drive-Link + PDF mit Preisen"
"Verarbeite neue Artikel von HotCakes Polewear: [Modell-Name]" → Cowork erkennt Shopify-Mapping und crawlt Storefront-JSON
"Verarbeite Cross-Selling-Refresh für HotCakes, Modell-Stamm Arachne" → Family-Refresh-Modus (E80-Erweiterung 3, v1.15)
```

### 2.4 Crawl-Mechanik (E48, 2026-05-15)

Cowork hat zwei komplementäre Crawl-Pfade:

**Pfad A — Firecrawl-Connector (geparkt, E41/B25):** für non-Shopify-Sites mit Anti-Bot-Komplexität. Aktuell nicht in Anthropic-Registry verfügbar. Wird reaktiviert sobald Connector-Aufnahme erfolgt.

**Pfad B — Code-Execution + Browser-UA + Shopify-Storefront-JSON (E48, aktiv):** für Shopify-gehostete Lieferanten-Sites. Mechanik:

1. Code-Execution-Sandbox mit `requests`, realistischem Browser-UA (Chrome aktuell), `Accept`/`Accept-Language`/`Sec-Fetch-*`-Header.
2. **Shopify-Detektion zuerst:** Homepage-GET mit `requests`, prüfen ob Set-Cookies `_shopify_*` zurückkommen. Wenn ja → Shopify, Pfad B greift. Wenn nein → kein Pfad-B-Crawl möglich, Halt-und-Nachfrage.
3. **Katalog-Listing:** `/products.json?limit=250&page=N`. Pagination-Ende = leeres `products`-Array. Bei <250 Produkten (HotCakes-Größenordnung: 124) reicht Page 1.
4. **Produkt-Detail:** `/products/<handle>.json` mit `body_html`, `options`, `variants`, `images`.
5. **Bild-Download:** `Accept`-Header mit `image/jpeg, image/png, image/webp;q=0.5, */*;q=0.1`. Plus **Magic-Byte-Detection** für echte Extension (A2 — Shopify-CDN liefert oft webp trotz `.jpg`-URL).
6. **`Accept-Encoding: gzip, deflate`** ohne `br` (Brotli-Modul nicht in der Cowork-Sandbox installiert).

**Lieferanten-Mapping** kann das Auto-Detektions-Ergebnis überschreiben über das optionale Feld `crawl_mechanik`:
- `shopify_json` — Pfad B erzwingen (oder bestätigen)
- `firecrawl` — Pfad A erzwingen, Lauf hält bis Firecrawl verfügbar
- `manual_only` — kein Crawl, nur Drive/Excel/PDF/Mail-Inputs

**Pole-Junkie-Sonderfall (E49):** Owner-Direktive Tjorben 2026-05-15 — Crawl-Freigabe für Pole-Junkie-Domain ohne Halt-und-Nachfrage. Im Lauf-Bericht E49-Verweis vermerken (Audit-Spur). Bei expliziter Cease-and-Desist-Forderung sofort eskalieren und pausieren.

---

## 3. Lieferantenkontext laden

**Quelle:** `lieferanten_mapping.yaml` aus dem **jüngsten Wissens-Snapshot** in Drive `Wichtig: Claude Backup/`.

**Resolution-Strategie** (ab E47, 2026-05-15) — bei jedem Pipeline-Lauf ein Mal ausführen am Stage-Start:

1. Liste alle Sub-Ordner im Live-Ordner `Wichtig: Claude Backup/` (parentId `12wDy0Z0cmB0p-OAs10Y7XqBWhmtQEip5`) mit Filter `title contains 'Version_' and mimeType = 'application/vnd.google-apps.folder'`.
2. Sortiere absteigend nach `title` — wegen Sub-Ordner-Namen-Format `Version_YYYY-MM-DD_HHMMSS` entspricht alphabetisch = chronologisch.
3. Iteriere durch die sortierten Sub-Ordner und nimm den ersten **kompletten** Sub-Ordner. Komplett = `_MANIFEST.md` UND alle in `SPEC_KONSTANTEN.md` Sektion 13 (`SNAPSHOT_KNOWLEDGE_FILES`) gelisteten Wissens-Files im Sub-Ordner vorhanden (Stand v1.17: 17 Wissens-Files + 1 Manifest pro Snapshot, inkl. der 6 ENTSCHEIDUNGS-LOG-Cluster nach v1.17-Split — Index in `SPEC_KONSTANTEN.md` Sektion 14, `ENTSCHEIDUNGSLOG_E_NUMMER_INDEX`). Check via einmaligem `search_files` mit `parentId = '<sub-folder-id>'`, dann gegen die in Sektion 13 gelistete File-Liste matchen. Unvollständige Sub-Ordner (Upload abgebrochen, Files fehlen) überspringen.
4. Lese `lieferanten_mapping.yaml` aus diesem Sub-Ordner via `download_file_content`. Bei `application/x-yaml`-Content den Roh-Inhalt parsen (kein Google-Conversion).

Diese Resolution-Strategie wird nicht nur für `lieferanten_mapping.yaml` verwendet, sondern für alle Wissens-Files (Charter, Entscheidungs-Log, Specs etc.). Cowork zieht damit immer den jeweils aktuellsten Wissens-Stand, unabhängig davon wie oft die Architektur sich entwickelt.

**Cowork resolved den Lieferanten** anhand des Anzeigenamens aus dem Trigger (Mapping `display_name → kuerzel`).

Besonders wichtig:
- `kuerzel`, `hersteller`, `herkunftsland`, `waehrung`, `steuerklasse` (für Stammdaten)
- `groessen_konvention` (`standard` oder `kombi_reduziert_auf_kleinste`, E27)
- `max_groesse` (NEU v1.15, optional) — Default-Größen-Cap pro Lieferant, falls Lieferant z.B. keine 2XL/3XL führt
- `category`, `crop_profile`, `pose_sort` (E45 — werden an Bildpipeline durchgereicht, beeinflussen Daten-Pipeline nicht direkt)
- `ameise_vorlagen.{stammdaten|variationen|merkmale|attribute|cross_selling}` (Naming gem. E29, 5 Vorlagen ab E80/v1.14)
- `lieferantennummer_wawi`, `r2_prefix`
- `text_quality` (`rich`/`thin`/`minimal`, B45) — falls gepflegt: steuert wie skeptisch Cowork Eigeninterpretation behandelt

Wenn Lieferant fehlt oder Pflichtfelder null: halten, beim User nachfragen.

---

## 3.1 Spec-Caching (E62, NEU v1.9)

**Pflicht-Konvention seit v1.9 (2026-05-16):**

Wissens-Files werden **einmalig zu Lauf-Beginn** aus dem jüngsten kompletten Snapshot geladen und lokal im Workspace gecacht. **Niemals pro Stage neu aus Drive geholt.**

**Begründung:** In mehreren End-to-End-Versuchen mit dem v1.8-Workflow verbrauchte Cowork ~50K Tokens nur für wiederholtes Lesen derselben Wissens-Files. Stage 0 (Wissens-Resolution) wurde nie überschritten, weil jede Stage erneut Drive-Reads triggerte. Die Konstanten-Auslagerung in `SPEC_KONSTANTEN.md` (E61) plus das Caching dieser Datei zu Lauf-Beginn löst beide Probleme zusammen.

**Konkretes Lade-Verhalten am Stage-Start:**

1. Snapshot-Resolution durchführen (siehe Sektion 3) → Sub-Folder-ID des jüngsten kompletten Snapshots.
2. Folgende Files **einmalig** via `download_file_content` herunterladen und lokal im Workspace ablegen (`/home/claude/wissens_cache/`):
   - `SPEC_KONSTANTEN.md` — kanonische Konstanten
   - `run_brief_daten.md` (NEU v1.13) — operative Essenz, Default-Loadable
   - `lieferanten_mapping.yaml` — Lieferanten-Kontext
   - **NICHT laden für Daten-Läufe:** `WAWI-IMPORT-WISSEN.md` und `cowork_anweisung_datenimports.md` (zu groß, triggern A8-Sub-Agent-Extraction) — `run_brief_daten.md` hat die operative Essenz daraus
   - **Lazy-Load nur bei Bedarf:** WAWI-IMPORT-WISSEN.md (z.B. bei tiefen Mapping-Klärungs-Situationen, wenn run_brief_daten.md nicht reicht)
3. **Alle weiteren Stages lesen ausschließlich aus dem lokalen Cache.** Bei Bedarf parsiert Cowork die gecachten Files (YAML, Markdown-Tabellen) ohne weiteren Drive-Roundtrip.
4. Bei Lauf-Ende: Cache wird verworfen (Workspace-Reset zwischen Läufen ist normal).

**Bei Drift-Verdacht (z.B. Tjorben sagt „der Snapshot wurde gerade aktualisiert"):** Lauf abbrechen, neu starten — kein Mid-Run-Reload.

**Gegenbeispiele (NICHT machen):**
- ❌ In jeder Stage erneut `download_file_content` für SPEC_KONSTANTEN.md aufrufen.
- ❌ Pro Artikel die Sprach-Lookup-Tabellen neu aus Drive holen.
- ❌ Self-Check-Checkliste pro Self-Check-Punkt einzeln aus Drive nachladen.

---

**Performance-Diagnose-Anforderung (NEU v1.15.1, BACKLOG B54):** Beim Spec-Caching jede File-Load-Wallclock dokumentieren (Drive-API-Roundtrip in Sekunden). Im Lauf-Bericht Sektion „Stages-Übersicht" pro File ausweisen. Trigger für BACKLOG-B54: wenn Stage 0 Total-Wallclock > 5 Min, im Lauf-Bericht-Note unter „Performance-Anomalien" explizit markieren.

## 4. Pipeline-Stages

Linear ohne User-Gates. Stop-Punkte nur bei harten Fehlern oder STOPP-Triggern aus E81.

### STOPP-Trigger (E81, NEU v1.15) — autonom überwacht

Cowork hält und fragt User **nur** bei diesen Bedingungen, **nicht** für Workflow-Details:

1. **Fehlende Pflicht-Daten:** Lieferant nicht im Mapping, Pflichtfeld im Mapping null, kritisches Datenfeld vom Input fehlend (Material, Preise, Farbe).
2. **Unbekannte Sprach-Begriffe außerhalb Lookup:** Begriff nicht in SPEC_KONSTANTEN.md Sektion 6 (Produkt-Substantiv-Tabelle oder Farb-Tabelle). Niemals raten (AP8).
3. **Goldstandard-Abweichungen:** Strukturelle Abweichung von den 3 Pilot-Artikeln (Hekate Bodysuit, Arachne Bottom Teal, Savanna Original Top) ohne Lieferanten-Mapping-Eintrag.
4. **Drift-Verdacht:** Wenn Tjorben oder ein Trigger-Wortlaut nahelegt, dass sich Mapping/Schema geändert hat.
5. **Cross-Selling-Family-Refresh ohne klare Scope-Definition:** wenn Trigger „Refresh" ist aber Modell-Stamm oder Lieferant unklar.

Alles andere wird **autonom entschieden** und im Lauf-Bericht dokumentiert. Insbesondere:
- Batch-Splitting bei großen Lieferungen (siehe Stage 0.5)
- Token-Budget-Reservierung pro Stage
- Stage-Reihenfolge bei parallelisierbaren Stages
- Cross-Selling-Stage-Aktivierung (greift automatisch bei ≥2 Artikeln in der Lieferung mit gleichem Modell-Stamm)

### Stage 0.5: Pre-Run Scope-Analyse (NEU v1.15, E83)

**Vor Stage 1.** Cowork schätzt das Lauf-Volumen:

- **Anzahl Modelle × durchschnittliche Größen pro Modell × Multi-Kategorie-Faktor 2** → Stammdaten-Zeilen
- **Anzahl Modelle × 5 Sprachen** → Variationen-Zeilen
- **Anzahl Artikel (Vater + Kinder) × Anzahl Merkmale pro Artikel** → Merkmale-Zeilen
- **Anzahl Artikel × Anzahl Attribute (6-7) × 5 Sprachen** → Attribute-Zeilen
- **Cross-Selling: Modelle pro Modell-Stamm × bidirektional × 5 Kinder-Replikation × 2 Gruppen** → CSV-Zeilen (E80-Erweiterung v1.15)

**Token-Schätzung:** ~2-3K Tokens pro Modell für Stammdaten/Variationen/Merkmale, ~8-12K Tokens pro Modell für Attribute (5 Sprachen, je 6 Attribute), plus Cross-Selling-CSV-Generierung.

**Batch-Schwelle:** wenn Schätzung >120K Tokens für einen Lauf, automatisch in Batches aufteilen.

**E84 Familien-erhaltende Split-Regel (NEU v1.15):** Outfit-Pair-Familien (gleicher Modell-Stamm, Top + Bottom mit gleicher Farbe) werden **niemals** über Batches gesplittet. Wenn ein Outfit-Paar in zwei verschiedenen Batches landen würde, wird der Batch-Cut so verschoben, dass die Familie zusammen bleibt. Cross-Selling-Stage 5.8 läuft im **letzten Batch** und sieht alle vorherigen Batches als gemeinsamen Scope (Stage 2 muss am Anfang des letzten Batches den vollen Lieferanten-Datensatz neu laden, oder über Batches hinweg cachen).

**Output Stage 0.5:** im Lauf-Bericht eine Sektion „Pre-Run Scope-Analyse":
```
Geschätzte Token: ~85K (Single-Batch)
Modelle: 10 (Batch 1 von 1)
Familien: 4 Outfit-Pair-Familien, alle in diesem Batch
Cross-Selling-Stage: ja (am Ende dieses Batches)
```

Bei Multi-Batch:
```
Geschätzte Token: ~180K → Aufteilung 2 Batches
Batch 1: Modelle 1-10 (Familien A, B; ~90K)
Batch 2: Modelle 11-21 (Familien C, D, E; ~95K)
Cross-Selling-Stage: in Batch 2 (vereint Scope beider Batches)
```

### Stage 1: Input erkennen & laden
- Lieferant + Input-Modus identifizieren
- Bei Mehrdeutigkeit: einmalig nachfragen
- Bei Crawl-Modus: Lauf halten mit Hinweis aus 2.4
- Daten in einheitliche interne Zwischenstruktur überführen
- **Cross-Selling-Family-Refresh-Modus erkennen (NEU v1.15):** wenn Trigger-Wortlaut „Refresh" oder „Family-Refresh" enthält, Stage 5.8 als alleinige Aktive Stage markieren, Stage 2-7 für CSVs 1-4 überspringen.

### Stage 2: Daten extrahieren

**firecrawl-Crawl (im Pilot nicht aktiv, E41/B25):**
- Wird derzeit nicht durchgeführt; Trigger bricht in Stage 1 ab.
- *Spec-Beschreibung für künftige Reaktivierung:* Aufruf über den im Cowork-Projekt installierten Firecrawl-MCP-Connector. Workflow: `/v2/map` → Produkt-URLs; `/v2/scrape` mit JSON-Schema-Extract pro Seite. Felder: `modellname`, `produkttyp`, `farbe`, `material`, `groessen`, `preis`, `beschreibung`, `bild_urls`, `lieferantenartikelnummer`. **Wenn primärer Retailer nicht alle Modelle führt:** automatisch auf `fallback_retailer_url` oder Hersteller-Site wechseln (E20). URLs nie aus Modellname+Farbe konstruieren — immer aus Listing-Seite extrahieren.

**Shopify-JSON-Crawl (E48, Pfad B):** mechanik in Sektion 2.4.

**PDF / Bild-im-PDF:** LLM-basiert, Lookbooks und Sortimentslisten erkennen.
**Excel/CSV:** Header-Zeile erkennen, Spalten mappen, bei nicht-Standard kurz nachfragen.
**Drive-Link:** Inhalt listen, Files nach Typ klassifizieren, Bilder separat für Bild-Pipeline sammeln.
**Mail-Inhalt:** LLM-strukturiert parsen, Klärungsfragen bei Lücken.

### Stage 3: Daten normalisieren

Einheitliche interne Liste:

```yaml
artikel:
  - modell: "Hekate Bodysuit"
    produkttyp_de: "Bodysuit"
    farbe_de: "Schwarz"
    lieferantenartikelnummer_basis: "HC-Hekate-Bodysuit"
    material_de: "82% Polyamid, 18% Elasthan"
    ek_netto: "39,00"
    groessen:
      - variant_value: "XS"       # nach groessen_konvention bereits reduziert
        suffix: "001"
      - variant_value: "S"
        suffix: "002"
    style_werte:
      style_tops: ["Bodysuit", "Open Back", "Rundausschnitt"]
      style_shorts: []
    bild_urls: ["https://...", "https://..."]    # Roh-URLs vom Lieferanten, werden an Bildpipeline durchgereicht
```

### Stage 4: Pricing berechnen (E25, Pilot-Vereinfachung)

```
GLD_netto = EK_Rechnung + Zoll_pro_Stück[Lieferant] + Versand_pro_Stück[Lieferant]
VK_brutto = GLD_netto × 2.0
          → gerundet auf X,90 mit Vollzehner-Unterbietung
            (rohes 78,00 → 77,90; rohes 40,10 → 39,90 statt 40,90)
```

**Referenztabelle:** `_PIPELINE/_Referenz/lieferanten_zoll_versand.csv` (Spalten `Lieferant; Zoll_avg_pro_Stück; Versand_avg_pro_Stück`). Lieferant nicht in der Tabelle → Zoll und Versand auf 0, im Bericht warnen.

**Aufschlagsfaktor 2.0** als Konstante für Kleidung-Pilot. Technik-Differenzierung kommt später (Charter-Prinzip 9, B18-Folgeaufgabe).

**Beispiel HotCakes Hekate Bodysuit:** EK 39,00 € → GLD 39,00 (Zoll 0, Versand 0) → VK roh 78,00 → VK 77,90 €.

### Stage 5: Mehrsprachige Felder ableiten (E26 + E31 + E55 + E56 + E58)

**Artikelname pro Sprache (Vater) — nach E58-Lookup-Tabellen aus SPEC_KONSTANTEN.md Sektion 6** (`{Hersteller} {Kleidungstyp} {Modell} {Farbe}`, ohne Größe):
- DE: `HotCakes Bodysuit Hekate Schwarz`
- EN: `HotCakes Bodysuit Hekate Black`
- FR: `HotCakes Body Hekate Noir`
- IT: `HotCakes Body Hekate Nero`
- ES: `HotCakes Body Hekate Negro`

**Kind-Artikelname (E56):** Vater-Sprachname + Leerzeichen + Variationswert (XS/S/M/L/XL/2XL). Beispiel Kind XS:
- DE: `HotCakes Bodysuit Hekate Schwarz XS`
- EN: `HotCakes Bodysuit Hekate Black XS`
- FR: `HotCakes Body Hekate Noir XS`
- IT: `HotCakes Body Hekate Nero XS`
- ES: `HotCakes Body Hekate Negro XS`

Vollständige Lookup-Tabellen in **SPEC_KONSTANTEN.md Sektion 6** (Produkt-Substantive + Farb-Adjektive). Bei Begriff außerhalb der Tabelle: STOPP + User-Frage in den Lauf-Bericht (E58, AP8).

**Print-Designs:** Artikelname bleibt simpel ohne Print-Bezeichnung. Print-Details kommen in `artikeldetails`.

**Variationen pro Sprache:** Größe / Size / Taille / Taglia / Talla. Werte (XS-2XL) universal, aber explizit pflegen.

**Meta-Daten (nur Vater, E55+E56):** Titel-Tag + Meta-Description pro Sprache. **Strikt deterministisch nach E55-Template** (siehe SPEC_KONSTANTEN.md Sektion 5). Einzige Variable ist `{name}` = Vater-Artikelname ohne Größe. Auf Kind-Zeilen sind alle SEO-Felder leer. Cowork generiert die SEO-Felder hardcoded aus den Templates, **niemals** via LLM-Generation (AP3).

### Stage 5.5: Attribut-HTML generieren (E22/E53/E74/E82-Stil)

**HTML-Konventionen:**
- **H1 wird NIE verwendet** — kollidiert mit Website-SEO. Pipeline-HTML nutzt H2 oder tiefer.
- **Em-Dashes (—) komplett vermeiden** — KI-Marker. Im Fließtext durch `,` ersetzen, in Taglines vermeiden.
- **Custom-CSS-Klassen:** Nur `check` und `h5 bold`.

**E82-Verschärfung (NEU v1.15):**
- **Doppelpunkte in `<h2>`-Taglines verboten:** statt `Material: Mesh` → `Mesh-Material` oder als ganze Phrase. Doppelpunkt im Tagline-Kontext wirkt Spec-Datenblatt-haft.
- **Doppelpunkte im Fließtext verboten** (außer in echten Aufzählungen mit nachfolgender Liste). Statt `Du brauchst:` → konkret formulieren.
- **Meta-Einleitungs-Sätze verboten:** „Die Maße:", „Die Pflege:", „Die Features:" — direkt mit dem Inhalt beginnen statt einleitenden Meta-Satz schreiben.

**Stilprofil (E22 + E74-Pivot ab v1.13):**

Zielgruppe: Frauen 25-35, fashionbegeistert, Pole-Dance-Performer oder -Lifestyle-Anhängerinnen. Outfits, die im Studio glänzen UND im Alltag funktionieren. Aspirational ansprechen, nicht ingenieurssachlich.

**Erlaubt:** Du-Form konsequent, warm-aspirational mit Esprit. Wohl gewählte starke Adjektive („verlängert optisch die Beine", „der mit dir mitatmet"). Kleine emotionale Anker. Fashion-Vokabular („Statement-Piece", „Wardrobe Essential", „geht von Studio zu Brunch"). Pole-Insider-Sprache („Floor Work", „Climb", „Grip", „Aerial Hoop"). Sinnliche Wendungen mit Maß.

**Verboten:** Schreierei-Superlative, Marketing-Klischees, Hashtags, Emojis, Werbe-Imperative, sexistische Anbiederung oder Objektifizierung. „Bottom" im deutschen Freitext (E76 — immer „Shorts"). Eingedeutschte Anglizismen („Polewear" bleibt, „Pole Dance" bleibt).

**Strukturelle Plagiate verboten (E77, NEU v1.14):** wörtliche 5-Wörter-Sequenzen aus Hersteller-Body, 1:1-Übernahme der Sub-Satz-Reihenfolge des Hersteller-Bodys, Pole-Junkie-Tagline-Imitationen. Cowork denkt komplett neu, nicht paraphrasiert/synonymisiert/umgestellt.

**Attribute pro Artikel (Stil-Modus pro Feld v1.14 — siehe SPEC_KONSTANTEN Sektion 11):**

| Attributname | Inhalt | Format (E22) | **Stil-Modus** |
|---|---|---|---|
| `markentext` | Brand-Pitch (80-150 Wörter, evergreen, Persönlichkeit) | `<h2>Marke</h2><p>Story</p>` | **E74-aspirational** (E72/E79 Caching im Mapping) |
| `artikeldetails` | Tagline + Kurz-Fließtext + Feature-Liste (E53/E74-Stil) | `<h2>Tagline</h2><p>1-2 Sätze</p><ul class="check"><li>Feature</li></ul>` | **E74-aspirational** (Kern-Verkaufstext) |
| `anwendung` | 3-8 Imperativ-Schritte (wenn Produkt-relevant) | `<ul class="check"><li>Schritt</li></ul>` | klar/funktional |
| `faqs` | Mehrere Blöcke à 30-80 Wörter (wenn Produkt-relevant) | wiederholtes `<h3>Frage?</h3><p>Antwort</p>` | warm-funktional |
| `material_and_care` | **2 Paragraphen: P1 Stoffzusammensetzung (EU-Pflicht), P2 Pflegehinweise** | `<p>...</p><p>...</p>` | **clean/funktional (E78, v1.14)** — siehe SPEC_KONSTANTEN Sektion 11.1 |
| `inhaltsstoffe` | Komma-Liste (wenn Produkt-relevant) | `<p>` | clean |
| `size_and_fit` | Passform-Text + Modellgröße + Tragehöhe (**keine Größentabelle** — zentral im Shop-Template) | Plaintext oder leichtes HTML | E74-aspirational gemäßigt |

**Mindestens** vier Kern-Attribute pro Artikel: `markentext`, `artikeldetails`, `material_and_care`, `size_and_fit`. Übrige je nach Produkt-Relevanz.

### Stage 5.6: ~~Bildpipeline-Sub-Process aufrufen~~ — DEAKTIVIERT mit E63 (2026-05-16)

Die Bildpipeline (`cowork_anweisung_bildpipeline.md`) ist mit E63 **archiviert**. Tjorben pflegt Bilder bis auf Weiteres manuell in WaWi. In dieser Pipeline-Version wird kein Bildpipeline-Sub-Process aufgerufen.

**Konsequenz für die Stammdaten-CSV:** Die 10 Bild-Spalten (`Bild 1` bis `Bild 10`) bleiben im Schema verpflichtend (Ameise-Vorlage erwartet sie), werden aber **mit leeren Strings** in jeder Vater- und Kind-Zeile ausgegeben.

### Stage 5.7: ~~Bild-URLs auf Vater + Kinder duplizieren~~ — DEAKTIVIERT mit E63

Entfällt mit E63. Alle Bild-Spalten (`Bild 1` bis `Bild 10`) werden auf Vater- und Kind-Zeilen mit leeren Strings befüllt. Wenn die Bildpipeline später reaktiviert wird, kommt die Duplizierungs-Logik unverändert zurück (E34 — JTL erbt nichts implizit).

### Stage 5.8: Cross-Selling-Beziehungen ableiten (v1.14 mit E80, v1.15 mit E80-Erweiterung)

**Voraussetzung:** Stage 2 hat den **vollen Lieferanten-Datensatz** im Speicher gehalten (z.B. alle 124 HotCakes-Produkte aus `/products.json`), nicht nur die Trigger-Modelle. Wenn nicht: Stage 2 wiederholen oder Beziehungen nur innerhalb der aktuellen Lieferung berechnen (eingeschränkter Scope, im Lauf-Bericht markieren).

**Family-Refresh-Modus (v1.15, E80-Erweiterung 3):** wenn Trigger „Refresh für Modell-Stamm X" oder „Family-Refresh" enthält, Cowork:
- skippt Stage 1-5.7 für CSVs 1-4
- läuft NUR Stage 5.8 für den gegebenen Modell-Stamm-Scope
- generiert nur `5_CrossSelling_<LIEFERANT>_<DATUM>.csv` als einzige Output-Datei
- Im Bericht explizit als „Cross-Selling-Family-Refresh-Lauf" markieren

**Algorithmus pro Vater-Artikel der Lieferung:**

1. **Identifiziere Modell-Stamm + Typ + Farbe** des aktuellen Artikels.
   - **Modell-Stamm-Schlüssel mit Farbe (v1.15, E80-Erweiterung 2):** `(modell_basis, farbe_im_namen)`. Beispiel: „Arachne Black" ist eine andere Modell-Familie als „Arachne Teal" für Outfit-Pair-Matching. Bug-Fix aus Live-Trial Batch 2 (2026-05-17): vor Fix wurden Arachne-Top-Black mit Arachne-Bottom-Teal gepaart, was semantisch falsch ist.
   - Modell-Basis: alles vor dem Typ-Identifier, z.B. „Peonies" aus „Peonies Top in Nude".
   - Typ: Top / Bottom / Bodysuit. (Im DE-Freitext „Shorts" — E76 — aber als interne Klassifikation bleibt es bei Top/Bottom/Bodysuit.)
   - Farbe: aus dem Shopify-Produkt-Titel oder Tags.

2. **Suche im vollen Datensatz nach „Vervollständige Dein Outfit"-Kandidaten:**
   - gleicher Modell-Stamm UND gleiche Farbe (Schlüssel: `(modell_basis, farbe_im_namen)`)
   - **gegensätzlicher Typ** (Top ↔ Bottom; Bodysuit hat kein Pendant → keine Beziehung)

3. **Suche im vollen Datensatz nach „Ähnliche Artikel"-Kandidaten:**
   - gleicher Modell-Stamm
   - **gleicher Typ**
   - **andere Farbe**

4. **Für jeden Treffer schreibe zwei Zeilen** in die Cross-Selling-Liste (A→B und B→A) — bidirektionale Sicherheits-Symmetrie.

5. **Kinder-Replikation (v1.15, E80-Erweiterung 1) — PFLICHT:**
   - **Linke Spalte (`Artikelnummer`):** Vater-Artikelnummer **UND alle Kind-Artikelnummern** (mit Größen-Suffix `-001`, `-002`, etc.)
   - **Rechte Spalte (`Artikelnummer Cross-Seller`):** **strikt Vater-Artikelnummer**, niemals Kind-IDs
   - **Cross-Selling-Gruppe:** unverändert
   - Bei N Größen pro Vater (typisch 5: XS/S/M/L/XL): pro bidirektionale Beziehung **2 × (1 + N) = 12 Zeilen** statt 2 (E80 v1.14 alt)
   - Live-Trial Batch 2 (2026-05-17): 11 Modelle, 16 bidir. Beziehungen → 180 Zeilen statt 36 (Faktor 5)

6. **Datenstruktur (interne Zwischenliste für Stage 7):**
   ```yaml
   cross_selling_beziehungen:
     - artikel: "HC-Peonies-Top-Nude"          # Vater
       cross_seller: "HC-Peonies-Bottom-Nude"
       gruppe: "Vervollständige Dein Outfit"
     - artikel: "HC-Peonies-Top-Nude-001"      # Kind XS, repliziert
       cross_seller: "HC-Peonies-Bottom-Nude"
       gruppe: "Vervollständige Dein Outfit"
     - artikel: "HC-Peonies-Top-Nude-002"      # Kind S
       cross_seller: "HC-Peonies-Bottom-Nude"
       gruppe: "Vervollständige Dein Outfit"
     # ... weitere Kinder
     - artikel: "HC-Peonies-Bottom-Nude"        # Vater (Gegenrichtung)
       cross_seller: "HC-Peonies-Top-Nude"
       gruppe: "Vervollständige Dein Outfit"
     # ... Bottom-Kinder replizieren
   ```

**Output dieser Stage:** interne Liste der Cross-Selling-Beziehungen für Stage 7 (CSV-Generierung).

**Scope-Hinweis:** Wenn die Trigger-Lieferung nur eine Teilmenge des Lieferanten-Sortiments umfasst (z.B. 10 Modelle aus 124), beziehen sich die Cross-Selling-Beziehungen trotzdem auf den **vollen** Datensatz. So landen Beziehungen wie „Peonies Top Nude → Peonies Top Beige" auch dann in der CSV, wenn nur Peonies Top Nude in der aktuellen Lieferung ist. WaWi-Cross-Selling-Anzeige funktioniert erst, wenn beide Artikel im Shop existieren — Beziehungen zu „noch nicht angelegten" Schwester-Artikeln werden beim ersten Re-Import nach deren Anlage aktiviert. Daher: keine Filterung, alle gefundenen Beziehungen in die CSV.

### Stage 6: Validierung (vor Output)

| Check | Verhalten bei Fehler |
|---|---|
| Lieferant im Mapping, Pflichtfelder gefüllt | Halten, nachfragen |
| Vater-/Kind-Lieferantenartikelnummer eindeutig | Lauf abbrechen, Duplikate melden |
| `Identifizierungsspalte Vaterartikel` jedes Kindes zeigt auf existierende Vater-Zeile | Lauf abbrechen |
| Vater in Merkmalen mit `Farbe Kleidung` + ggf. Style | Lauf abbrechen |
| **Kind in Merkmalen mit `Farbe Kleidung`, Style (falls anwendbar), `Größe Kleidung`** (E19) | Lauf abbrechen |
| **Vater + alle Kinder in Attributen** (E34) | Lauf abbrechen |
| **Bild-Spalten `Bild 1`-`Bild 10` sind in jeder Zeile vorhanden** (auch wenn leer, wegen E63 standardmäßig leer) | Lauf abbrechen — Schema-Konformität |
| **Standardlieferant in Vorlagen-Konfiguration explizit gesetzt** (Self-Check 16, v1.15) | Lauf abbrechen + User-Frage |
| Merkmalwerte aus erlaubter Liste (siehe SPEC_KONSTANTEN.md Sektion 7) | Lauf abbrechen |
| Sprach-Spalten (Artikelname, Variationen, Meta-Daten) nicht leer | Lauf abbrechen |
| Preise numerisch mit Komma | Lauf abbrechen |
| `EK Netto (für GLD)`, `Brutto-VK`, `Netto-EK`, `Lieferzeit in Tagen (Lieferant)` für alle Zeilen gefüllt | Lauf abbrechen |
| **Cross-Selling-Beziehungen (v1.15): linke Spalte Vater + Kinder repliziert, rechte Spalte strikt Vater** (Self-Check 15) | Lauf abbrechen |
| **Datei-Naming AP11-konform** (`<NR>_<Typ>_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv`) | Vor `present_files` Datei umbenennen |
| **AP12: keine leeren CSVs** (z.B. Cross-Selling ohne Beziehungen) | Datei weglassen, im Bericht vermerken |

Bei Fehler: keine partielle Ausgabe. Entweder alle CSVs konsistent oder gar keine.

#### Stage 6 Mapping-Bibel-Self-Check (E59, verpflichtend) — siehe SPEC_KONSTANTEN.md Sektion 9

**🔒 Kanonische Quelle:** `SPEC_KONSTANTEN.md` Sektion 9 enthält die 16-Punkte-Self-Check-Checkliste (12 alte + 4 neue v1.15: 13 E77-Plagiats-Check, 14 E78-Material-Pattern, 15 Cross-Selling-Kinder-Replikation, 16 Standardlieferant-Setting), das Output-Format pro Punkt (`[#N] [✓/✗] <Punkt> — <Detail>`) und das Fail-Verhalten (STOPP, eindeutige Benennung, User-Frage formulieren). Plus Sektion 8 dort: Goldstandard-Referenz-Artikel (Hekate Bodysuit, Arachne Bottom Teal, Savanna Original Top) und Sektion 10 dort: Anti-Patterns AP1-AP12 (AP9-AP12 NEU v1.15).

**Cowork-Pflicht:** Vor Stage 7 (CSV schreiben) müssen alle 16 Punkte durchlaufen werden. Im Lauf-Bericht pro Punkt eine `[✓/✗]`-Bestätigung dokumentieren. Bei Fail eines Punkts: Lauf abbrechen, Punkt eindeutig benennen, User-Frage formulieren.

### Stage 7: CSVs schreiben

Ablage (E52 final, E69 Drift-Korrektur v1.12, AP10 verschärft v1.15):
- **CSVs:** `/home/claude/outputs/` im Cowork-Workspace. Via `present_files`-Pattern an Tjorben ausgegeben.
- **Lauf-Bericht:** ebenfalls `/home/claude/outputs/`, parallel zu den CSVs. Via `present_files` mit ausgegeben.
- **KEIN Drive-Upload für CSVs oder Lauf-Bericht** (AP10, verschärft v1.15). A6-Workaround (gzip+base64+Chunking) ist mit E69 final archiviert. Bug-Beleg Live-Trial Batch 1 (2026-05-17): Cowork hat trotz AP10 3 Files in Drive geladen (korrupte Versionen wegen base64-Chunking-Verlust), siehe BACKLOG B51 für Cleanup-Workaround. Falls Tjorben Dateien dauerhaft in Drive will, lädt er sie nach dem Lauf manuell hoch.

**Datei-Naming (AP11, Pflicht v1.15):** Pattern `<NR>_<Typ>_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv`. Beispiele:
- `1_Stammdaten_HOTCAKES_2026-05-17_2230.csv`
- `2_Variationen_HOTCAKES_2026-05-17_2230.csv`
- `3_Merkmale_HOTCAKES_2026-05-17_2230.csv`
- `4_Attribute_HOTCAKES_2026-05-17_2230.csv`
- `5_CrossSelling_HOTCAKES_2026-05-17_2230.csv`

NR ist 1-5, Typ in CamelCase (kein Bindestrich, kein Underscore innerhalb Typ), LIEFERANT in UPPERCASE aus `kuerzel`. Bug-Beleg: ohne AP11 hat Cowork in Live-Trial Files ohne NR-Präfix erzeugt, was Tjorben in Ameise erschwerte.

**AP12: keine leeren CSVs (NEU v1.15).** Wenn eine Stage 0 Zeilen produziert (z.B. Stage 5.8 ohne Cross-Selling-Beziehungen), die Datei **nicht** schreiben. Im Lauf-Bericht entsprechend vermerken: „Stage 5.8: keine Cross-Selling-Beziehungen gefunden, 5_CrossSelling-CSV nicht erstellt".

Globale Format-Regeln:

| Parameter | Wert |
|---|---|
| Encoding | UTF-8 mit BOM (`utf-8-sig`) |
| Trennzeichen | `;` |
| Quoting | minimal für Stammdaten/Variationen/Merkmale/Cross-Selling; `QUOTE_ALL` für Attribute |
| Zeilenende | CRLF |
| Dezimaltrennzeichen | Komma |

**Output-Mechanik (E52-Pivot ab v1.8, 2026-05-15 Abend):**

Im 3-Modell-Batch-Lauf 2026-05-15 hat der Drive-Upload **55,9 % der Wallclock-Zeit** verbraucht (1268 s von 2269 s). Plus: das Tool-Output-Limit von ~50 K Zeichen führte beim Upload größer Attribut-CSVs (107 KB) zu partial-Uploads. Tjorbens Workflow (CSVs direkt aus Workspace per Chat-Download für Ameise-Import) macht das Drive-Archiv für CSVs überflüssig.

**Architektur ab v1.8:**

```
5 CSVs → /home/claude/outputs/<dateiname>.csv (lokal, AP11-Naming)
       → Cowork ruft am Ende den present_files-Pattern auf
       → Tjorben downloadet alle 5 CSVs direkt im Chat
       → Tjorben importiert in Ameise

Lauf-Bericht → /home/claude/outputs/run_<datum>_<lieferant>.md (lokal)
            → KEIN Upload nach Drive (AP10 v1.15)
            → via present_files mit ausgegeben

Mapping-Cheatsheet → /home/claude/outputs/Mapping_<lieferant>.md (lokal)
                  → KEIN Upload nach Drive (AP10 v1.15)
                  → via present_files mit ausgegeben
```

```python
# Output-Pattern für 5 CSVs (lokal, kein Drive-Upload):
csv_paths = []
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
for nr, typ, csv_content in [
    (1, "Stammdaten", stammdaten_content),
    (2, "Variationen", variationen_content),
    (3, "Merkmale", merkmale_content),
    (4, "Attribute", attribute_content),
    (5, "CrossSelling", cross_selling_content),
]:
    if not csv_content or not csv_content.strip():  # AP12-Check
        bericht += f"\nStage für {typ}: keine Zeilen produziert, CSV nicht erstellt.\n"
        continue
    path = f"/home/claude/outputs/{nr}_{typ}_{LIEFERANT.upper()}_{timestamp}.csv"  # AP11-Naming
    with open(path, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write(csv_content)
    csv_paths.append(path)

# Bericht + Cheatsheet: lokal (AP10 v1.15)
bericht_path = f"/home/claude/outputs/run_{timestamp}_{LIEFERANT}.md"
# ... write bericht ...
cheatsheet_path = f"/home/claude/outputs/Mapping_{LIEFERANT}.md"
# ... write cheatsheet ...

# Am Ende: alle Files dem User präsentieren
present_files(filepaths=csv_paths + [bericht_path, cheatsheet_path])
```

`base64Content` ist obsolet für die Pipeline-Outputs — alle Files sind UTF-8-Text. Für Bilder/Binary gilt R2 als Ablage (E44), nicht Drive.

**Mapping-Cheatsheet pro Lauf (E54-Begleitung, NEU v1.8):**

Cowork generiert pro Lauf eine kleine Markdown-Datei `Mapping_<lieferant>.md` die Tjorben beim Vorlagen-Mapping in Ameise unterstützt:

```markdown
# Spalten-Mapping HotCakes — Schema v3.1 (Lauf 2026-05-17_2230)

| Pos | CSV-Spalte | JTL-Feld | Hinweis |
|---:|---|---|---|
| 1 | Artikelnummer | Artikelnummer | Auto |
| 2 | Artikelnummer (Lieferant) | Artikelnummer (Lieferant) | Auto |
... (alle 48 Positionen)
| 39 | Bild 1 | Bild Pfad/URL 1 | Manuell |
| 40 | Bild 2 | Bild Pfad/URL 2 | Manuell |
...

Plus operative Settings:
- Reiter „Bilder/Plattformen": alle 11 Häkchen
- Reiter „Verkaufskanal aktiv": alle Häkchen ENTFERNEN
- „Standardwert Währung" = EUR
- „Identifizierungsspalte Vaterartikel" = Artikelnummer
- **Standardlieferant: HOTCAKES (v1.15 Pflicht)** — in jeder der 5 Vorlagen explizit setzen
```

Bei Schema-Bumps (z.B. v3.1 → v4) wird der Cheatsheet automatisch mit aktualisierten Positionen generiert.

**Schema-Migration-Konvention (E54, NEU v1.8):**

- Schema-Bumps werden im ENTSCHEIDUNGS-LOG vermerkt (E-Eintrag mit Schema-Version-String, z.B. „Schema v3.2")
- **Append-only:** neue Spalten werden grundsätzlich AM ENDE angehängt, NICHT in bestehende Bereiche eingefügt
- Bei jedem Schema-Bump dokumentiert Cowork im Lauf-Bericht eine Migration-Notiz, die Tjorben über die Vorlagen-Anpassung informiert
- Tjorben kann vor dem Bump die bestehende Vorlage als `<Vorlagenname>_v<N>_archiv` duplizieren um Rollback zu ermöglichen

---

## 5. CSV-Schemas im Detail

> ## 🔒 WAWI-IMPORT-MAPPING-BIBEL — KANONISCH (E59, ab v1.9 in SPEC_KONSTANTEN.md)
>
> **Konstanten leben jetzt in `SPEC_KONSTANTEN.md`** (E61, ab v1.9). Diese Sektion gibt die Struktur (Schema-Übersicht, Variationen, Attribute, Stil-Briefing), verweist für alle harten Konstanten (48-Spalten-Schema, SEO-Templates, Sprach-Lookup, Merkmalwerte, Self-Check, Anti-Patterns) auf `SPEC_KONSTANTEN.md`. Cowork hat die **Pflicht**, sowohl diese Anweisung als auch `SPEC_KONSTANTEN.md` **vor jeder CSV-Generation** zu konsultieren — siehe Mapping-Bibel-Self-Check in Stage 6.
>
> **Niemals durch generierte Plausibilität ersetzen.** Bei Lücke oder Unsicherheit: STOPP + User-Frage in den Bericht, niemals erfinden. Charter-Prinzipien 10 + 11.
>
> **Goldstandard-Referenz:** Hekate Bodysuit (`HC-Hekate-Bodysuit`), Arachne Bottom Teal (`HC-Arachne-Bottom-Teal`), Savanna Original Top (`HC-Savanna-Original-Top`) — Details siehe SPEC_KONSTANTEN.md Sektion 8.

### 5.1 Stammdaten — siehe SPEC_KONSTANTEN.md

**🔒 Kanonische Quelle:** `SPEC_KONSTANTEN.md` Sektionen 1-4.

Diese Sektion definiert in v1.9+ keine Konstanten mehr selbst, sondern verweist auf SPEC_KONSTANTEN.md:

- **Sektion 1 dort:** 48-Spalten-Schema v3.1 (exakte Reihenfolge, Positionen 1-48)
- **Sektion 2 dort:** Standardwerte für Kleidung-Pilot (Steuerklasse, TARIC, Gewicht, Versandklasse, Herkunftsland-Default, Bestandsführung, Neu im Sortiment, Ist Standardlieferant, Lieferzeit)
- **Sektion 3 dort:** Kategorie-Mapping pro Kleidungstyp (E51) — Ebene 1 immer `Pole Dance Kleidung`, Ebene 2 aus erlaubter Liste
- **Sektion 4 dort:** Vater-Kind-Konventionen (E26/E56/E57/E58) — inkl. Multi-Kategorie-Doppelzeilen

**Hinweis Bild-Spalten in v1.10 (E63):** Bildpipeline ist archiviert, Tjorben pflegt Bilder manuell in WaWi. Die 10 Bild-Spalten (Position 39-48) bleiben im Schema verpflichtend, werden aber **standardmäßig mit leeren Strings** ausgegeben.

### 5.1.1 SEO-Templates — siehe SPEC_KONSTANTEN.md Sektion 5

**🔒 Kanonische Quelle:** `SPEC_KONSTANTEN.md` Sektion 5 enthält die deterministischen Titel-Tag- und Meta-Description-Templates pro Sprache (DE/EN/FR/IT/ES, inkl. HTML-Entities `&#10004;` und `&#10148;`).

**Cowork-Pflicht:** Hardcoded aus den Template-Strings befüllen. **Keine LLM-Generation** für SEO-Felder (AP3). Einzige Variable: `{name}` = Vater-Artikelname **ohne Größe**.

### 5.1.2 Sprach-Lokalisierung — siehe SPEC_KONSTANTEN.md Sektion 6

**🔒 Kanonische Quelle:** `SPEC_KONSTANTEN.md` Sektion 6 enthält die Lookup-Tabellen für Produkt-Substantive (Bodysuit/Shorts/Top/Leggings × 5 Sprachen) und Farb-Adjektive (12 Standard-Farben × 5 Sprachen) sowie die Liste der **niemals zu lokalisierenden** Begriffe (Brand-Namen, Modell-Eigennamen, Größen).

**Cowork-Pflicht:** Bei Begriff außerhalb der Tabellen → **STOPP + User-Frage** im Lauf-Bericht, niemals raten (AP8).

### 5.2 Variationen (12 Spalten)

```
Artikelnummer; Variationsname; Darstellungsform; Variationswertname;
Global-Englisch: Variationsname; Global-Englisch: Variationswertname;
Global-Französisch: Variationsname; Global-Französisch: Variationswertname;
Global-Italienisch: Variationsname; Global-Italienisch: Variationswertname;
Global-Spanisch: Variationsname; Global-Spanisch: Variationswertname
```

Eine Zeile pro Größen-Variante. `Artikelnummer` = Vater-Artikelnummer. `Darstellungsform` = `DROPDOWN`. Variationsname pro Sprache aus E26-Tabelle.

### 5.3 Merkmale (4 Spalten, E19/E34, E50)

```
Lieferant; Artikelnummer (Lieferant); Merkmalname; Merkmalwertname 1
```

**Pro Artikel mehrere Zeilen — auf Vater UND Kind explizit gepflegt** (E19, validiert JTL-Export 13.05.2026).

**Sprache: NUR Deutsch in der CSV.** WaWi pflegt die Übersetzungen statisch pro Merkmalwert intern. Cowork generiert AUSSCHLIESSLICH die deutschen Werte.

**🔒 Kanonische Quelle für Merkmalwerte + zweistufige Farb-Logik:** `SPEC_KONSTANTEN.md` Sektion 7 enthält die statischen WaWi-Merkmalwert-Listen (`Farbe Kleidung` 15, `Größe Kleidung` 6, `Style Tops` 11, `Style Shorts` 11) und die zweistufige Farb-Logik (spezifischer Name im Artikelnamen, nächstpassender WaWi-Wert im Merkmal) plus Mapping-Hilfe für häufige Sonderfälle (Teal→Blau, Nude→Beige, Burgund→Rot, etc.).

**Wichtig (operative Erinnerung):** `Style Bodysuits` und `Style Leggings` existieren **nicht** als Merkmalsnamen. Bodysuits laufen über `Style Tops` mit Wert „Bodysuit" plus weitere Top-Style-Werte.

### 5.4 Attribute (8 Spalten, alle Felder gequotet) — Standard nach E39, Stil-Update E53

```
Lieferant; Artikelnummer (Lieferant); Attributname; Attributwert;
Englisch: Attributwert; Französisch: Attributwert; Italienisch: Attributwert; Spanisch: Attributwert
```

**Pro Artikel mehrere Zeilen — auf Vater UND Kind explizit gepflegt** (E34, analog zu Merkmalen). Alle Felder gequotet (`QUOTE_ALL`) — Attribute enthalten HTML mit Sonderzeichen.

**Attribute pro Artikel (Pipeline-Scope, Stil-Modus pro Feld v1.14 — siehe SPEC_KONSTANTEN Sektion 11):**

Siehe Stage 5.5 oben. Mindestens vier Kern-Attribute: `markentext`, `artikeldetails`, `material_and_care`, `size_and_fit`. E82-Stilregeln gelten (Doppelpunkt/Meta-Einleitungs-Verbot).

### 5.5 Cross-Selling (3 Spalten, E80 v1.14, Kinder-Replikation v1.15)

```
Artikelnummer; Artikelnummer Cross-Seller; Cross-Selling-Gruppe
```

**Algorithmus:** siehe Stage 5.8.

**Quoting:** minimal.

**v1.15-Pflicht-Mechanik:**
- linke Spalte (`Artikelnummer`): Vater + alle Kinder repliziert
- rechte Spalte (`Artikelnummer Cross-Seller`): strikt Vater
- bidirektional doppelt (A↔B in zwei Zeilen)
- Cross-Selling-Gruppen müssen vorab in WaWi existieren (`Vervollständige Dein Outfit`, `Ähnliche Artikel`)

### 5.6 ~~Bilder~~ — entfallen mit E46, **eingefroren mit E63 (2026-05-16)**

Bilder werden nicht mehr als separate CSV ausgegeben. Sie leben als Spalten `Bild 1` bis `Bild 10` in der Stammdaten-CSV (siehe 5.1).

**Stand v1.9+ (E63):** Die Bildpipeline ist **archiviert** — `cowork_anweisung_bildpipeline.md` ist nicht aktiv. Tjorben pflegt Bilder bis auf Weiteres manuell in WaWi. Die 10 Bild-Spalten in der Stammdaten-CSV werden mit **leeren Strings** befüllt (Schema-Konformität erhalten, Ameise-Vorlage erwartet die Spalten). Stage 5.6 und 5.7 sind in dieser Version deaktiviert.

**Re-Aktivierung:** Sobald der Bilder-Architektur-Refactor abgeschlossen ist (siehe `BACKLOG.md` Cluster „Bilder-Architektur-Refactor"), kommt die Bildpipeline mit einer überarbeiteten Architektur zurück.

### 5.7 Feature-Erfassungs-Quellen (E70, v1.12)

Nach E63 (Bildpipeline archiviert) bleibt die Frage offen, wie Farbe, Style-Werte und andere Features in die Pipeline kommen. Antwort: **text-basiert** — und das war auch in der archivierten Bildpipeline schon so, dort gab's nie eine Vision-basierte Feature-Extraktion (nur Pose-Sortierung).

**Quellen für Features (in dieser Priorität):**

1. **Shopify-Titel / Lieferanten-Produktname** — primäre Quelle für Modellname, oft auch für Farbe.
2. **Body_HTML / Lieferanten-Produktbeschreibung** — Material, Schnitt, Features, Style-Werte. Hauptquelle bei Shopify-Lieferanten.
3. **PDF/Mail-Texte** (bei Drive/Excel/PDF/Mail-Input-Modi) — analog Body_HTML.
4. **Pole-Junkie-Schwestermodell als Cross-Reference** (v1.12) — wenn der Hersteller-Text dünn ist und Pole Junkie das Modell oder ein Schwestermodell führt, darf Cowork die Pole-Junkie-Produktseite zusätzlich aufrufen und Features daraus ableiten (E49-Direktive + E70 erweitert). Bisher (E49/E53) war Pole Junkie nur Stil-Inspirations-Quelle für `artikeldetails`. NIE Copy-Paste, Eigenformulierung in polesportshop-DNA.

**Konvention bei Eigeninterpretation:**

Wenn ein Style-Wert oder Feature nicht eindeutig aus den Text-Quellen ableitbar ist (z.B. „athletic cut at the back" → Cowork interpretiert als `Open Back`), muss Cowork das im Lauf-Bericht **explizit als Interpretation markieren**. Format: ein eigener Abschnitt „Eigeninterpretationen" mit Quell-Text, gewähltem Wert und Begründung. Tjorben prüft im visuellen Self-Check in WaWi.

**Was NICHT erlaubt ist:**

- Vision-API für Feature-Extraktion aufrufen (Pilot-Pragmatik, kommt später, siehe BACKLOG-Cluster „Feature-Erfassung")
- Style-Werte raten, wenn der Text nichts hergibt — dann STOPP + User-Frage (Charter-Prinzip 10)
- Eigeninterpretationen im Lauf-Bericht verschweigen — Transparenz ist Pflicht

---

## 6. Ameise-Vorlagen-Naming (E29, ab v1.14 = 5 Vorlagen pro Lieferant nach E80)

Pro Lieferant **5 Vorlagen** einmalig angelegt (zuvor 4 mit E46, +1 mit E80). Konvention:

`{Lieferantenname}_{Reihenfolge}_{Import-Typ}`

— Underscores als Element-Trenner, Leerzeichen nur innerhalb des Lieferantennamens.

**Reihenfolge ab v1.14 (E80):**

- `HotCakes Polewear_1_Stammdaten` (inkl. Bild-Spalten und Bilder/Plattformen-Konfiguration)
- `HotCakes Polewear_2_Variationen`
- `HotCakes Polewear_3_Merkmale`
- `HotCakes Polewear_4_Attribute`
- `HotCakes Polewear_5_CrossSelling` **(NEU v1.14, E80)** — Ameise-Import-Typ „Cross-Selling-Artikel", 3 Spalten: Artikelnummer + Artikelnummer Cross-Seller + Cross-Selling-Gruppe

**Standardlieferant in jeder Vorlage Pflicht (NEU v1.15):** in jeder der 5 Vorlagen muss in den Vorlagen-Settings der Standardlieferant explizit gesetzt sein. Bug-Beleg Live-Trial Batch 1 Attribute-Import 2026-05-17: `_4_Attribute`-Vorlage hatte Standardlieferant auf „nicht gewählt", was zu 220 Warnungen „Lieferant HOTCAKES existiert nicht" beim Import führte. Die CSV liefert den Lieferanten zwar als Spalte, aber Ameise erwartet zusätzlich das Vorlagen-Default-Setting.

**Slot-Konvention pro Import-Typ (NEU v1.15):** Slot-Nummern sind eindeutig **pro Import-Typ**, NICHT lieferanten-weit. Eine `_3_Merkmale`-Vorlage hat denselben Slot wie eine `_3_Lieferantendaten`-Vorlage, aber unterschiedlichen Import-Typ — das ist OK, weil Ameise pro Import-Typ filtert. Bei HotCakes mit historischer Anlage:

- `HotCakes Polewear_3_Lieferantendaten` — Slot 3 in Import-Typ „Artikeldaten des Lieferanten" (Legacy, vor E35 angelegt, ohne Funktion seit E35)
- `HotCakes Polewear_3_Merkmale` — Slot 3 in Import-Typ „Artikelmerkmale" (aktuell, korrigiert v1.15 — war vorher als `_4_Merkmale` dokumentiert)
- `HotCakes Polewear_5_Bilder` — Slot 5 in Import-Typ „Artikelbilder pro Plattform" (Legacy, vor E46 angelegt, ohne Funktion seit E46)
- `HotCakes Polewear_5_CrossSelling` — Slot 5 in Import-Typ „Cross-Selling-Artikel" (aktuell, produktiv v1.15)

Bestehende Vorlagen NICHT umnummerieren (Aufwand vs. Nutzen). Legacy-Vorlagen bleiben in WaWi ohne Funktion.

**Bestand HotCakes (final v1.15):** 5 aktive Vorlagen wie oben + 2 Legacy. Die Attribute-Vorlage wurde 2026-05-16 von Tjorben angelegt. Die `_5_CrossSelling`-Vorlage wurde vor Live-Trial Batch 1 angelegt und in Batch 1+2 erfolgreich produktiv eingesetzt.

**Bestand POLE ADDICT:** folgt noch altem Naming (`POLE ADDICT Stammdaten Import` etc.). Nicht umbenennen — alte Vorlagen funktionieren. Stammdaten-Vorlage muss um Bild-Spalten erweitert werden, alte Bilder-Vorlage (`POLE ADDICT Bilder Import`) wird Legacy. Cross-Selling-Vorlage beim Onboarding neu anzulegen.

---

## 7. Spalten-Mapping in Ameise

**Generelle Regel (E30):** Spaltennamen müssen nicht zwanghaft JTL-Feldnamen treffen. Pro Lieferant einmal manuell mappen + Vorlage speichern, dann pro neuem Lieferanten klonen. Sprechende Namen sind OK.

**Speziell Stammdaten:**
- `Brutto-VK` greift Auto-Mapping (validiert HotCakes-Lauf)
- `EK Netto (für GLD)` greift Auto-Mapping **nicht** — manuelle Zuordnung im Mapping-Dialog auf das JTL-Feld "Ø Einkaufspreis (netto)", dann Vorlage speichern (E28/E38)
- `Identifizierungsspalte Vaterartikel` → JTL-Feld "Vaterartikel ID-Feld"
- `Vaterartikel identifizieren anhand` = `Artikelnummer`, `Vaterartikel-ID-Feld ist` = `Artikelnummer`
- Varkombi-Behandlung = "Variationen und Werte im Vaterartikel erstellen"
- **Lieferantenblock-Spalten** (`Netto-EK`, `Ist Standardlieferant`, `Lieferzeit in Tagen (Lieferant)`) im Bereich "Lieferanteneinstellungen des Artikels" der Vorlage zuordnen. **Standardwert "Währung"** in der Vorlage auf den Lieferanten-Wert setzen (z.B. EUR für HotCakes), nicht als CSV-Spalte (E36).
- **Bild-Spalten (NEU mit E46)** `Bild 1` bis `Bild 10` der Vorlage zuordnen → JTL-Felder `Bild Pfad/URL 1` bis `Bild Pfad/URL 10`.
- **Reiter „Bilder/Plattformen" der Vorlage:** alle 11 Plattform-Häkchen setzen. Damit aktiviert JTL beim Stammdaten-Import jedes gefüllte Bild automatisch auf allen 11 Plattformen — Plattform-Aktivierung läuft ohne nachgelagerten Schritt (B5-Lösung über E46).
- **Multi-Kategorie-Einstellung (NEU mit E57):** In den Vorlagen-Einstellungen die Option **„Kategorieverknüpfungen des Artikels aktualisieren"** auf den Wert **„Neue Kategorien beim jeweiligen Artikel hinzuimportieren"** setzen. Default ist „Nicht aktualisieren" — dann werden Multi-Kategorie-Doppelzeilen funktionslos. Vorlage anschließend speichern (gilt session-übergreifend). Setting-Name in Ameise 1.10.15.0 ist „Kategorieverknüpfungen des Artikels aktualisieren", in älterer Forum-Doku auch „Aktualisierung von Kategorien eines Artikels" genannt — funktional identisch.

  - **🔒 Anti-Confusion-Note (E75, NEU v1.13):** Wenn jemand „doppelte Größen" oder „Stammdaten-Zeilen doppelt vorhanden" als Bug meldet — **KEIN Spec-Eingriff in E57**. Die Doppelzeilen-Architektur ist gewollt (Forum-recherchiert, Re-Import-validiert, siehe E57 + E75 im LOG). Erst prüfen: ist das Vorlagen-Setting oben korrekt gesetzt? Wenn nicht → Setting fixen, originale CSV nochmal importieren. Wenn ja und Symptom bleibt → erst dann Architektur-Diskussion. **Niemals eine „gefixte" CSV ohne Doppelzeilen bauen, ohne diesen Cross-Check zuerst.** Goldstandard-Referenz: `1_Stammdaten_HotCakes_2026-05-16.csv` (im Pilot-Hauptordner) — funktioniert mit Doppelzeilen + korrektem Setting sauber.
- **Standardlieferant (NEU v1.15)** in den Vorlagen-Einstellungen explizit setzen (z.B. HOTCAKES). Bug-Beleg: 220 Warnungen ohne dieses Setting.

**Reiter "Weitere Texte" — wichtig (E31):**
Unten in Ameise. Tabelle *Datenfeld / Sprache / Spalte in Importdatei*. Pro Sprache (EN/FR/IT/ES):
- "Artikelname, {Sprache}" → CSV `Global-{Sprache}: Artikelname`
- "Titel-Tag, {Sprache}" → CSV `Global-{Sprache}: Titel-Tag`
- "Meta-Description, {Sprache}" → CSV `Global-{Sprache}: Meta-Description`

Analog beim Variationen-Import (Variationsname/Variationswertname pro Sprache).

**Verkaufskanal aktiv (rechts oben):**
Defaultmäßig alle Häkchen gesetzt. **Bei Vorlagen-Anlage Häkchen in Vorlage entfernen und Vorlage speichern** (E37) — sonst gehen Artikel sofort online. Tjorben aktiviert nach Shop-Review pro Artikel manuell. Mittelfristig pro CSV-Spalte (B21).

> **Wichtige Unterscheidung:**
> - „Verkaufskanal aktiv" steuert, ob der **Artikel** in einem Verkaufskanal sichtbar ist → soll im Pilot deaktiviert sein, manuell pro Artikel aktivieren nach Review (E37/B21).
> - „Bilder/Plattformen" steuert, ob die **Bilder** auf einer Plattform aktiv sind → soll für alle 11 Plattformen in der Vorlage aktiviert sein, damit Bilder beim Stammdaten-Import direkt auf allen Plattformen scharf geschaltet werden (E46/B5-Lösung).
> Die beiden Reiter sehen ähnlich aus, steuern aber unterschiedliche Dinge.

**Cross-Selling-Vorlage (NEU v1.14):** Ameise-Import-Typ „Cross-Selling-Artikel" wählen (im Menü „Artikel" eigene Sektion, **nicht** Teil von „Artikeldaten"). 3 Spalten zuordnen:
- `Artikelnummer` → Identifizierungsspalte (Artikelnummer)
- `Artikelnummer Cross-Seller` → Artikel-IDs Cross-Selling-Artikel (Artikelnummer)
- `Cross-Selling-Gruppe` → Cross-Selling-Gruppe
- **Standardlieferant explizit setzen (v1.15 Pflicht)**

---

## 8. Reihenfolge der Imports

1. **Stammdaten** (Artikel > Artikeldaten) — inkl. Bilder und Lieferantenblock; muss zuerst, sonst gibt's keinen Artikel
2. **Variationen** (Artikel > Variationen) — Sprach-Werte für Größe
3. **Merkmale** (Artikel > Artikelmerkmale) — Filter / Such-Index
4. **Attribute** (Artikel > Artikelattribute) — Reichtext-Inhalte
5. **Cross-Selling** (Cross-Selling-Artikel — eigene Sektion) — Beziehungen zwischen Artikeln

> **Historische Hinweise:**
> - Bis v1.2 stand zwischen Variationen und Merkmalen ein eigener Lieferantendaten-Import. Mit E35 ist der entfallen — Lieferanten-Felder kommen jetzt direkt im Stammdaten-Import mit.
> - Bis v1.4 stand nach Attributen ein separater Bilder-Import (Bilder > Artikelbilder pro Plattform). Mit E46 (2026-05-15) ist der entfallen — Bild-URLs kommen jetzt direkt im Stammdaten-Import mit, Plattform-Aktivierung läuft automatisch über die Vorlage.
> - Bis v1.13 war Cross-Selling manuelle Pflege in der WaWi-Artikelmaske. Mit E80 (v1.14) als 5. CSV automatisiert, in Live-Trial Batch 1+2 (v1.15, 2026-05-17) produktiv erprobt.

---

## 9. Fehler-Handling

| Situation | Verhalten |
|---|---|
| Lieferantenname nicht im Mapping | Halten, beim User nachfragen |
| Pflichtfelder im Mapping null | Halten, fehlende Werte abfragen |
| `groessen_konvention` fehlt | Default `standard`, im Bericht warnen |
| `category` / `crop_profile` / `pose_sort` fehlt | Default `fashion` / `fashion` / `auto_vision`, im Bericht warnen |
| `max_groesse` fehlt | Default null (kein Cap), im Bericht erwähnen |
| Input-Modus nicht eindeutig | Halten, klären |
| **Crawl-Trigger mit Shopify-Detektion erfolgreich (E48 Pfad B)** | Crawl durchführen via Code-Execution + Storefront-JSON. Im Bericht E48-Pfad markieren. |
| **Crawl-Trigger ohne Shopify-Erkennung, kein Firecrawl-Connector** | Lauf halten, User auf manuellen Drive/Excel/PDF-Workaround verweisen (E41/B25 — Firecrawl nicht in Cowork-Registry). Falls Lieferant `crawl_mechanik: shopify_json` im Mapping hat aber Site offenbar nicht Shopify ist: User informieren und manuell nachverfolgen. |
| **Pole-Junkie-Crawl (E49 Owner-Direktive)** | Crawl ohne Halt-und-Nachfrage durchführen. Im Bericht E49-Verweis. Bei Cease-and-Desist-Forderung sofort eskalieren und pausieren. |
| Primärer Retailer unvollständig (im künftigen Crawl-Modus) | `fallback_retailer_url` oder Hersteller-Site, ohne stoppen |
| Übersetzung scheitert bei einzelnem Feld | Artikel in `_Review/`, andere weiter |
| Pflichtfeld fehlt (Material, Preise, Farbe) | Lauf abbrechen, präzise melden |
| Lieferant nicht in `lieferanten_zoll_versand.csv` | Zoll/Versand auf 0, im Bericht warnen |
| Merkmalwert außerhalb erlaubter Liste | Lauf abbrechen (B19 künftig vorab) |
| **Bildpipeline-Sub-Process (E63 deaktiviert)** | Stage 5.6 entfällt, Bild-Spalten mit leeren Strings befüllen, kein Halt nötig |
| Validierung scheitert | Lauf abbrechen, keine partielle Ausgabe |
| **Stage 5.8 ohne Cross-Selling-Beziehungen** (AP12) | 5_CrossSelling-CSV nicht erstellen, im Bericht vermerken |
| **Datei-Naming nicht AP11-konform** | Vor `present_files` umbenennen |
| Cloud-Storage-Link (Dropbox/WeTransfer/...) | NICHT blind fetchen — Connector prüfen oder User um lokalen Download bitten |
| **Family-Refresh-Trigger ohne klare Modell-Stamm-Definition** | STOPP + User-Frage: welcher Modell-Stamm soll refresht werden? |

---

## 10. Konventionen

### Was Cowork DARF
- Dateien anlegen, lesen, kopieren
- Drive-Connector für Wissens-Files und Lieferanten-Drive-Ordner nutzen
- Übersetzungen erstellen (innerhalb E58-Lookup; bei seltenen Begriffen mit Markierung)
- HTML-Snippets nach E22-Templates generieren (mit E82-Stilregeln)
- CSVs validieren und schreiben
- WaWi (read-only) abfragen
- `lieferanten_mapping.yaml` und `lieferanten_zoll_versand.csv` lesen
- Bildpipeline programmatisch als Sub-Process aufrufen (sobald E63-Archivierung aufgehoben — aktuell nicht aktiv)
- **Autonom Workflow-Entscheidungen treffen** (Batch-Splitting, Token-Budget, Stage-Reihenfolge — E81)

### Was Cowork NICHT DARF
- Dateien permanent löschen
- WaWi schreibend ändern
- Importvorlagen in Ameise verändern
- A-Nummern vergeben
- Ohne User-Bestätigung `lieferanten_mapping.yaml` schreiben
- `lieferanten_zoll_versand.csv` schreiben (das macht der Buchhaltungs-Connector, B17)
- API-Keys oder Credentials im Chat ausgeben oder als ad-hoc-Trigger-Parameter akzeptieren (E33)
- **Bild-Spalten in der Stammdaten-CSV mit Hersteller-CDN-URLs befüllen** (E44 hartcodiert — Validierung Stage 6 bricht ab, wenn keine R2-Public-URL erkannt wird). Aktuell mit leeren Strings befüllen (E63).
- **Produkt-spezifische Meta-Descriptions oder Titel-Tags erfinden** (E55 — Templates sind hardcoded, einzige Variable ist `{name}`). Generation via LLM für SEO-Felder ist strikt verboten — Cowork füllt direkt aus den E55-Template-Strings (AP3).
- **Sprach-Namen außerhalb der E58-Lookup-Tabellen erfinden.** Bei Begriff, der nicht in den Tabellen steht (z.B. exotische Farbe): STOPP, in den Lauf-Bericht als User-Frage markieren — niemals raten (AP8).
- **Eigennamen übersetzen** (Modell-Namen, Brand-Namen wie „Hekate", „Arachne", „HotCakes"). E58 — diese bleiben in allen 5 Sprachen unverändert.
- **Schema-Spalten-Reihenfolge umorganisieren.** E54 ist append-only — neue Spalten kommen am Ende, niemals in bestehende Bereiche eingefügt (AP4).
- **Kategorie-Werte außerhalb der E51-Tabelle nutzen.** „Damen" und „Limited Editions" sind keine gültigen Kategorien für Kleidungs-Pilot (AP1).
- **Multi-Kategorie-Zuweisung ohne Doppelzeilen umsetzen.** Es gibt keine alternative Mechanik — pro Artikel zwei CSV-Zeilen mit gleicher Artikelnummer + Ameise-Setting (E57, AP6).
- **Kind-Artikelname ohne Größen-Suffix lassen.** Kind-Name in allen 5 Sprachen = Vater-Sprachname + Leerzeichen + Variationswert (E56, AP5).
- **SEO-Felder auf Kind-Zeilen befüllen.** Titel-Tag und Meta-Description leben nur auf Vater-Zeilen (E56).
- **Doppelpunkte in `<h2>`-Taglines oder im Fließtext setzen** (E82, NEU v1.15). Self-Check 13 prüft das.
- **Meta-Einleitungs-Sätze schreiben** wie „Die Maße:" oder „Die Pflege:" (E82, NEU v1.15).
- **Cross-Selling-Kinder-Replikation überspringen** (E80-Erweiterung v1.15, AP-Self-Check 15). Pflicht: linke Spalte Vater + alle Kinder.
- **CSVs ohne AP11-Naming schreiben** (NEU v1.15). Pflicht: `<NR>_<Typ>_<LIEFERANT>_<YYYY-MM-DD_HHMM>.csv`.
- **Leere CSVs erstellen** (AP12, NEU v1.15). Bei Stage ohne Output Datei weglassen und im Bericht vermerken.
- **CSVs nach Drive uploaden** (AP10, verschärft v1.15). Bug-Beleg Live-Trial Batch 1: 3 korrupte Uploads in Drive trotz AP10. Strikt im Workspace lassen, Tjorben downloadet via `present_files`.

### Datenstrategien (aktueller Stand)

**A-Nummer-Strategie aufgeschoben (E6):** Artikelnummer = Lieferantenartikelnummer.

**Plattform-Aktivierung (B5) — GELÖST durch E46:** Bilder werden über die Stammdaten-CSV mit Spalten `Bild 1`-`Bild 10` eingebracht; Ameise-Vorlage hat im Reiter „Bilder/Plattformen" alle 11 Plattform-Häkchen gesetzt; Aktivierung läuft beim Stammdaten-Import automatisch. (Aktuell wegen E63 mit leeren Strings befüllt.)

**Verkaufskanal-Aktivierung beim Import (B21/E37):** Aktuell Häkchen in Vorlage entfernen. Mittelfristig CSV-Spalten mit Default "N".

**URL-Slug-Robustheit:** Niemals URLs aus Modellname+Farbe konstruieren — immer aus Listing-Page extrahieren (relevant sobald Crawl-Modus reaktiviert wird, B25).

**Crawl-Modus geparkt (E41/B25):** Firecrawl ist im Pilot nicht aktiv. Bei Crawl-Bedarf manueller Workaround: Sortimentsliste aus Lieferanten-Shop exportieren und als Drive/Excel/PDF reinkippen. Pfad B (Shopify-JSON, E48) aktiv für Shopify-Lieferanten.

### Idempotenz
- Wiederholter Lauf mit identischem Input erzeugt identische CSVs (bis auf Zeitstempel)
- Mehrfacher Lauf am selben Tag: alte CSVs nicht überschreiben, parallel ablegen (Sekundengenauigkeit im Timestamp möglich)

### Re-Import-Verhalten bei leeren Bild-Spalten (UNVERIFIZIERT — B30)

Bei einem Stammdaten-Re-Import eines bestehenden Artikels, dessen Bild-Spalten 4 bis 10 leer sind, ist das JTL-Verhalten noch nicht final geklärt:
- *Verhalten A (gewünscht):* leerer Wert = kein Update, vorhandenes Bild im Slot bleibt erhalten
- *Verhalten B (problematisch):* leerer Wert = Slot wird aktiv geleert, vorhandenes Bild verschwindet

Die Konvention im Pilot ist: pro Lauf immer alle 10 Spalten in der CSV ausgeben (mit Leer-Strings, wenn weniger Bilder). Die Vorlage erwartet die fixen 10 Spalten. Verifikation des Verhaltens steht aus (siehe BACKLOG B30) — bis dahin keine Re-Imports auf bestehende Artikel mit weniger als 10 Bildern.

### Re-Import-Verhalten bei Cross-Selling (UNVERIFIZIERT — B49, teilvalidiert v1.15)

Bei Initial-Import (Live-Trial Batch 1+2 2026-05-17) hat die Mechanik produktiv funktioniert. Re-Import-Verhalten auf bestehende Beziehungen (Family-Refresh-Modus) ist noch nicht validiert. Bis Verifikation: vor Re-Import alle Cross-Selling-Beziehungen des betroffenen Lieferanten in WaWi manuell löschen, dann frischer Import. Sobald validiert: Anweisung an Cowork-Lauf-Bericht.

---

## 11. Credentials und externe Services

Innerhalb des Cowork-Setups gibt es zwei zulässige Credential-Mechanismen (E33, erweitert 2026-05-15):

1. **Connector-Setup in der Cowork-UI** — API-Keys werden beim Hinzufügen eines MCP-Connectors einmalig in der Cowork-Settings-UI eingegeben (aus Dashlane). Cowork ruft den Service danach über den Connector. Aktuell verbunden: Google Drive, Cloudflare Developer Platform. Künftig (bei Registry-Aufnahme): Firecrawl (B25), eventuell Cloudflare-Code-Mode (B26).

2. **Drive-Credentials-File mit eingeschränktem Zugriff** — für Services ohne nativen Connector. Im Pilot betrifft das ausschließlich die R2-Object-Upload-Mechanik in der Bildpipeline (E43, siehe `cowork_anweisung_bildpipeline.md` v1.3). Für die Daten-Pipeline (dieses Dokument) ist aktuell kein zweites Drive-Credential-File nötig.

**Egress-Allowlist (B29):** Network-Egress-Modus „All domains" als Pilot-Default wegen Anthropic-Bug (Issues #38984, #51400 — der granulare „Package managers only"-Modus ignoriert die Additional-Liste silent). Reversibel sobald Bug-Fix kommt.

Was bleibt strikt verboten: API-Keys über den Chat-Input weitergeben oder als ad-hoc-Parameter setzen lassen — auch nicht in Test-/Probe-Sessions. Cowork hat in mehreren Setup-Versuchen 2026-05-15 solche Chat-Key-Versuche selbst als E33-Anti-Pattern geflaggt und abgelehnt; diese Eskalation ist die gewünschte Behaviour.

---

## 12. Verwandte Dokumente

- **`SPEC_KONSTANTEN.md` (kanonisch ab v1.9, E61)** — **🔒 KANONISCHE** Quelle für alle harten Konstanten dieser Pipeline (48-Spalten-Schema, SEO-Templates, Sprach-Lookup, Merkmalwerte, Self-Check 16-Punkte, AP1-AP12). Charter-Prinzip 11.
- **`run_brief_daten.md` (kanonisch ab v1.13, E68)** — operative Essenz für Daten-Läufe, Default-Loadable in Stage 0 statt der großen Spec-Files.
- **`cowork_custom_instructions.md` (NEU v1.13)** — globale Cowork-Instruktionen (Workspace-Setup, Tool-Permissions, Output-Konventionen).
- `cowork_anweisung_bildpipeline.md` v1.6 — **ARCHIVIERT mit E63** (2026-05-16). Nicht aktiv ausgeführt. Tjorben pflegt Bilder bis auf Weiteres manuell in WaWi. Wissens-Referenz für späteren Architektur-Refactor (siehe BACKLOG Cluster „Bilder-Architektur-Refactor").
- `lieferanten_mapping.yaml` — Single Source of Truth Lieferanten-Metadaten. Bild-Felder (`crop_profile`, `pose_sort`, `category`) bleiben für spätere Bildpipeline-Reintegration im Schema. NEU v1.15: optional `max_groesse`.
- `WAWI-IMPORT-WISSEN.md` — **🔒 KANONISCHES** operatives Pilot-Wissen (CSV-Schemas, Stolperfallen, validiert in echten Läufen, v1.15 mit Live-Trial-Batch-1+2-Erkenntnissen). Anti-Pattern-Sektion 10.5 ist mit v1.9 in `SPEC_KONSTANTEN.md` Sektion 10 gewandert (v1.15 erweitert auf AP12).
- ENTSCHEIDUNGS-LOG (seit v1.17 in 6 Themen-Cluster gesplittet — Index aller E-Nummern auf die jeweiligen Cluster-Files in `SPEC_KONSTANTEN.md` Sektion 14, `ENTSCHEIDUNGSLOG_E_NUMMER_INDEX`). Inhaltlich relevant für diese Spec: E14 (Firecrawl), E19/E34 (Erbung-Verbot), E22 (HTML/Stil), E23/E25 (Pricing), E26 (Artikelname), E27 (Größen-Konvention), E28/E38 (GLD), E29 (Vorlagen-Naming, jetzt 5 Vorlagen ab E80), E30 (Spalten-Mapping), E31 (Mehrsprachigkeit), E32 (Cowork-Setup), E33 (Credential-Mechanismen), E35 (5 CSVs — historisch), E36 (Stammdaten 38 Spalten — historisch), E37 (Verkaufskanal), E39 (Attribute Standard), E41 (Crawl-Tool-Marktcheck), E42 (Local MCP Bridge tot), E43 (R2-Upload-Mechanik), E44 (R2 als vollständiger Storage), E45 (Crop-Profile + Pose-Sortierung), E46 (Bilder in Stammdaten, 48 Spalten), E50 (WaWi-Merkmalwerte + zweistufige Farb-Logik), E51 (Kategoriebaum-Mapping), E52 (A6-Pivot), E53 (Stilidentität), E54 (Schema-Layout v3.1), E55 (SEO-Templates pro Sprache), E56 (Kind-Artikelname mit Größen-Suffix), E57 (Multi-Kategorie via Doppelzeilen), E58 (Sprach-Lokalisierungs-Konvention), E59 (WaWi-Mapping als Fels), E60 (Bild-Größen-Cap, v2.0), **E61 (Konstanten-Auslagerung in SPEC_KONSTANTEN.md), E62 (Spec-Caching), E63 (Bildpipeline archiviert), E68 (Selective Spec-Loading + Run-Brief), E69 (A6-Drift-Korrektur), E70 (Pole-Junkie als Feature-Cross-Reference), E72/E79 (Caching im Mapping), E73 (Mehrsprachigkeit voll alle 5), E74 (Stil-Pivot aspirational), E75 (Anti-Confusion-Note E57), E76 (Shorts im DE-Freitext), E77 (Anti-Plagiarism), E78 (Material-Pattern clean), E80 (Cross-Selling als 5. CSV), E80-Erweiterung v1.15 (Kinder-Replikation + Modell-Stamm-Schlüssel mit Farbe + Family-Refresh), E81 (Autonomie-Hoheit), E82 (Stil-Verschärfung Doppelpunkt), E83 (Pre-Run Scope-Analyse), E84 (Familien-erhaltende Split-Regel)**
- `PROJEKT-CHARTER.md` — Prinzip 10 (E59, WaWi-Mapping als gefrorenes Wissen) + **Prinzip 11 (E61, Konstanten-Datei-Architektur)** + v1.15-Erweiterungen für E81-E84
- `BACKLOG.md` — B5 GELÖST, B17/B18 (Pricing-Vorbedingungen), B19 (Merkmalswerte-Validierung), B21 (Verkaufskanal-Aktivierung), B22 TEILGELÖST, B25 (Firecrawl-Registry), B26 (Cloudflare-Code-Mode), B27 (Worker-Proxy), B28 (Vision-Klassifikations-Verifikation), B29 (Allowlist-Bug-Tracker), B30 (Re-Import-Verhalten), B33 (Drive-MCP-Limits, verschärft v1.15), B35 (Bild-Größen-Cap), B47 (Cross-Selling-Skalierung, verschärft v1.15), B49 (Re-Import-Verhalten Cross-Selling, teilvalidiert v1.15), B51 (Drive-Cleanup-Workaround NEU v1.15), B52 (Schwester-Artikel-Liste NEU v1.15), B53 (Skalierungs-Validierung NEU v1.15), plus **neue Cluster** (Bilder-Architektur-Refactor, Bildpipeline-Performance, WaWi-Update-Validation)
