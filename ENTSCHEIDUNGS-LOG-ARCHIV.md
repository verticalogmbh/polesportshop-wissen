# Entscheidungs-Log — ARCHIV

> **Hinweis v1.16 (2026-05-17):** Diese Datei enthält Architektur-Entscheidungen, die durch nachfolgende Entscheidungen **abgelöst** wurden oder die eine **historische/transitorische Phase** dokumentieren, die heute nicht mehr aktiv gilt. Die volle Begründung jedes Eintrags bleibt hier erhalten — als Audit-Spur und als Schutz davor, dass spätere Sessions bereits verworfene Sackgassen wiederholen.
>
> **Verhältnis zu `ENTSCHEIDUNGS-LOG.md` (AKTIV):** Verweise aus anderen Wissens-Files auf hier archivierte E-Nummern sind absichtlich erhalten — sie sind Audit-Spur, kein Drift. Der Resolver lädt beide Dateien parallel.
>
> **Inhalt:** 6 Einträge (E14, E20, E35, E36, E40, E42), chronologisch nach E-Nummer geordnet, jeweils mit Cluster-Kontext aus der ursprünglichen AKTIV-Datei.

---

## Übersicht der archivierten Einträge

| E-Nummer | Titel (Kurzform) | Ursprünglicher Cluster | Abgelöst durch |
|---|---|---|---|
| E14 | firecrawl statt eigene Scraping-Lösung | Crawling & Quellen | E41, E48 (Crawl-Tool-Strategie + Pfad B Shopify-JSON) |
| E20 | Hersteller-Site als bevorzugte Crawl-Quelle bei unvollständigem Ret... | Crawling & Quellen | E48, E49 (Crawl-Modus B + Pole-Junkie-Freigabe) |
| E35 | Lieferantendaten-CSV abgeschafft → integriert in Stammdaten-CSV | Cowork-Projekt-Architektur (2026-05-14, präzisiert 2026-05-15) | E46, E54 (Bilder in Stammdaten, 48-Spalten-Schema) |
| E36 | Stammdaten-Schema v2 mit 38 Spalten (3 neue Lieferantenblock-Spalten) | Cowork-Projekt-Architektur (2026-05-14, präzisiert 2026-05-15) | E54 (Stammdaten-Schema v3.1, 48 Spalten) |
| E40 | Hersteller-CDN-URLs in Bilder-CSV als Übergangslösung | Cowork-Projekt-Architektur (2026-05-14, präzisiert 2026-05-15) | E43, E44 (R2-Upload-Mechanik + R2 als vollständiger Storage) |
| E42 | Local MCP via `claude_desktop_config.json` ist in Cowork-Sessions n... | R2-Pfad und Cowork-Realität (neu 2026-05-15) | (weiterhin gültige Realität, dokumentiert in Charter und E32/E33) |

---

## E14

*Ursprünglicher Cluster: «Crawling & Quellen» — abgelöst durch: E41, E48 (Crawl-Tool-Strategie + Pfad B Shopify-JSON)*

**E14 — firecrawl statt eigene Scraping-Lösung.**
*Warum:* LLM-Extract built-in, Anti-Bot-Behandlung erledigt, billig genug (~30-60 Credits/Lauf).
*Verworfen:* Eigenes Scraping (Maintenance-Hölle). web_fetch-only in Cowork (keine strukturierte Extraktion).
*Verfügbarkeit (Stand 2026-05-15):* Firecrawl ist **nicht** als nativer Cowork-Connector in der Anthropic-Registry verfügbar. Alternativen (Tavily, Brightdata) wurden im Marktcheck 2026-05 evaluiert, Firecrawl bleibt strategisch beste Wahl (siehe E41). Crawl-Modus im Pilot geparkt, bis Firecrawl in der Registry erscheint (B25).

---

## E20

*Ursprünglicher Cluster: «Crawling & Quellen» — abgelöst durch: E48, E49 (Crawl-Modus B + Pole-Junkie-Freigabe)*

**E20 — Hersteller-Site als bevorzugte Crawl-Quelle bei unvollständigem Retailer-Sortiment.**
*Warum:* Pole Junkie EU führte im HotCakes-Lauf nicht alle Rechnungsmodelle (kein Mauve, kein Sky). Hersteller-Site `hotcakespolewear.com` hatte alle 11 Rechnungsmodelle. Retailer dienen als Fallback für Detail-Daten und alternative Modellfotos.
*Verworfen:* Nur Retailer-Crawl. Hätte zu fehlenden Varianten geführt.

---

## E35

*Ursprünglicher Cluster: «Cowork-Projekt-Architektur (2026-05-14, präzisiert 2026-05-15)» — abgelöst durch: E46, E54 (Bilder in Stammdaten, 48-Spalten-Schema)*

**E35 — Lieferantendaten-CSV abgeschafft → integriert in Stammdaten-CSV.**
*Stand:* 2026-05-14.
*Warum:* Die in v1.2 als separate CSV vorgesehene Lieferantendaten-Pflege (Netto-EK, Währung, Lieferzeit) lässt sich beim Stammdaten-Import in JTL-Ameise direkt mitgeben — im Bereich "Lieferanteneinstellungen des Artikels" stehen die relevanten Felder zur Verfügung. Charter-Prinzip 9 ("Klein nach groß") hat gewirkt: separate CSV war Overengineering, ein zusätzlicher Import-Schritt ohne Mehrwert.
*Neue Pipeline (5 CSVs nach 2026-05-14, 4 CSVs nach E46 ab 2026-05-15):*
1. Stammdaten (inkl. Lieferantenblock-Spalten, ab E46 auch inkl. Bild-URL-Spalten) — Import-Typ *Artikel > Artikeldaten*
2. Variationen — Sprach-Varianten Größe — Import-Typ *Artikel > Variationen*
3. Merkmale — Filter-Indizes — Import-Typ *Artikel > Artikelmerkmale*
4. Attribute — Reichtext-Inhalte — Import-Typ *Artikel > Artikelattribute*
5. ~~Bilder~~ — entfällt nach E46, Bild-URLs leben jetzt in der Stammdaten-CSV
*Konsequenz für bestehende Vorlagen:* HotCakes-Vorlage `_3_Lieferantendaten` wird nicht mehr genutzt, bleibt als Legacy in WaWi stehen. Stammdaten-Vorlage wurde um die 3 Lieferantenblock-Spalten ergänzt (E36) und um Bild-URL-Spalten (E46). HotCakes-Vorlage `_5_Bilder` wird nach E46 nicht mehr genutzt, bleibt als Legacy stehen.
*Verworfen:* Separate Lieferantendaten-CSV beibehalten (mehr Import-Schritte ohne funktionalen Gewinn). Komplett-Verzicht auf Lieferantenblock (würde Netto-EK in Originalwährung nicht im System haben).

---

## E36

*Ursprünglicher Cluster: «Cowork-Projekt-Architektur (2026-05-14, präzisiert 2026-05-15)» — abgelöst durch: E54 (Stammdaten-Schema v3.1, 48 Spalten)*

**E36 — Stammdaten-Schema v2 mit 38 Spalten (3 neue Lieferantenblock-Spalten).**
*Stand:* 2026-05-14. Bezug: E35. *Update 2026-05-15:* Schema v3 mit 48 Spalten nach E46 (10 neue Bild-URL-Spalten).
*Warum (v2):* Mit der Integration der Lieferantendaten in die Stammdaten-CSV (E35) wachsen die 35-Spalten der v1 auf 38 Spalten. Die 3 neuen Spalten kommen direkt nach dem Preise-Block:
- `Netto-EK` (Rechnungspreis in Originalwährung des Lieferanten, z.B. `39,00` EUR für HotCakes Hekate)
- `Ist Standardlieferant` (Y/N, Default Y — bei Pilot ein Lieferant pro Artikel)
- `Lieferzeit in Tagen (Lieferant)` (numerisch, Default 0)
*Tjorben hat verworfen:* Brutto-EK (Marken-Steuer-Logik überflüssig im Pilot), USt. in % (über Steuerklasse abgebildet), Artikelname (Lieferant) (Lieferant verwendet eh denselben Namen), Währung als CSV-Spalte (besser Standardwert in der Ameise-Vorlage).
*Befüllung:* Vater + alle Kinder erhalten dieselben Werte (Lieferantenblock gilt pro Lieferanten-Artikel-Beziehung, nicht pro Variante).
*Validierung:* HotCakes-Stammdaten-v2-Import 2026-05-14 mit 16 Zeilen erfolgreich.
*Erweiterung v3 (E46, 2026-05-15):* 10 zusätzliche Bild-URL-Spalten am Ende der CSV: `Bild 1; Bild 2; ...; Bild 10`. Default-Anzahl ist 10 (deckt 95%+ der Produkte ab, JTL erlaubt bis 20). Leere Spalten erlaubt wenn ein Artikel weniger Bilder hat. Damit wächst das Schema von 38 auf 48 Spalten.

---

## E40

*Ursprünglicher Cluster: «Cowork-Projekt-Architektur (2026-05-14, präzisiert 2026-05-15)» — abgelöst durch: E43, E44 (R2-Upload-Mechanik + R2 als vollständiger Storage)*

**E40 — Hersteller-CDN-URLs in Bilder-CSV als Übergangslösung. — ABGELÖST 2026-05-15**
Übergangs-Workaround für den ersten HotCakes-Bildpipeline-Versuch (R2-Connector im Cowork-Projekt noch nicht installiert), nicht E10-konform. Vollständig abgelöst durch E43 (R2-Upload-Mechanik) und E44 (R2 als vollständiger Storage). Arachne-Bottom-Black-Migration 2026-05-15 hat die Mechanik validiert; Hekate Bodysuit + Arachne Top Black folgen sobald Bild-Beschaffung läuft (B22 teilgelöst).

---

## E42

*Ursprünglicher Cluster: «R2-Pfad und Cowork-Realität (neu 2026-05-15)» — abgelöst durch: (weiterhin gültige Realität, dokumentiert in Charter und E32/E33)*

**E42 — Local MCP via `claude_desktop_config.json` ist in Cowork-Sessions nicht sichtbar.**
*Stand:* 2026-05-15. Bezug: Charter Prinzip 9, E33.
*Warum:* In Settings → Developer existiert ein „Local MCP servers"-Bereich mit Edit-Config-Button, der die `claude_desktop_config.json` öffnet. Die UI suggeriert, dass dort registrierte MCP-Server in Cowork-Sessions sichtbar werden. Probe-Test 2026-05-15: Tjorben hat `@modelcontextprotocol/server-filesystem` mit `/Users/tjorbenbecker/Downloads/mcp-probe` als Pfad in der Config registriert, Claude Desktop neu gestartet, Cowork-Session geöffnet und nach dem `test-filesystem`-Namespace gefragt. Ergebnis: gelbes Warnbanner in der Cowork-UI „MCP test-filesystem: Server disconnected", keine `mcp__test-filesystem__*`-Tools im Namespace, keine `read_file`/`list_directory`-Aufrufe möglich. Cowork-Host liest den Config-Eintrag zwar (versucht den Server zu starten), aber die Tools werden nicht in die Cowork-Tool-Surface gebrückt.

*Konsequenz:* Local MCP via Desktop-Config ist für Cowork-Pipelines **kein gangbarer Weg**. Alle externen System-Anbindungen für Cowork-Pipelines müssen entweder:
- Cloud-Connectors aus der Anthropic-Registry sein (Google Drive, Cloudflare Developer Platform, künftig Firecrawl), oder
- Code-Execution + Network-Egress in der Cowork-Sandbox nutzen (mit user-konfigurierter Domain-Allowlist und Credentials via Drive-File gem. E33).

*Vollständiges Probe-Result:* `_PIPELINE/_Logs/2026-05-15_crawl-tool-evaluation/local_mcp_probe_result.md` (Drive-ID `1raSOVGlQKBDMZCeEkDqc-OPJnQ4aQ_Dn`).

*Verworfen:* Annahme, dass Settings → Developer eine Cowork-Bridge ist. War Spec-Hoffnung, nicht verifizierter Stand — siehe Charter Prinzip 9. Pfad (a) bei B22 (S3-MCP-Server via Local-MCP-Bridge gegen R2-Endpoint) wurde mit diesem Probe-Ergebnis verworfen.

*Generalisierbares Pattern (zu Charter Prinzip 9):* Vor Verankerung eines neuen Tool-/Connector-Mechanismus in einer Spec mit Probe-Test verifizieren — registrieren → fragen → bestätigen. Verifikations-Pattern explizit in E33-Block aufgenommen.
