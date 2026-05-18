# ENTSCHEIDUNGS-LOG-LIVE-TRIAL

**Cluster:** Live-Trial-Konsolidierung E81-E84

**Stand:** v1.17, 2026-05-17

**Bezug:** Dieser Cluster ist Teil des Splits der ursprünglichen `ENTSCHEIDUNGS-LOG.md` (v1.16, 165 KB → 6 Themen-Cluster ≤ 40 KB). Historische / abgelöste Einträge liegen weiterhin in `ENTSCHEIDUNGS-LOG-ARCHIV.md`. Cross-Cluster-Referenzen über E-Nummer; der Master-Index mit allen E-Nummern → Cluster-File-Zuordnung liegt in `SPEC_KONSTANTEN.md` unter `ENTSCHEIDUNGSLOG_E_NUMMER_INDEX`.

---

## Index

- **E81** — Autonomie-Hoheit für Workflow-Entscheidungen
- **E82** — Stil-Verschärfung — Doppelpunkt-Verbot und Meta-Einleitungs-Verbot
- **E83** — Pre-Run Scope-Analyse als Stage 0.5
- **E84** — Familien-erhaltende Split-Regel

---

**E81 — Autonomie-Hoheit für Workflow-Entscheidungen.**
*Stand:* 2026-05-17.

**Trigger:** Wiederholte Beobachtung in mehreren Daten-Läufen vor und während Live-Trial Batch 1+2: Cowork hat in der v1.14-Pipeline häufig User-Fragen gestellt zu Workflow-Details, die operativ klar definiert waren (Batch-Größe, Stage-Reihenfolge, Token-Budget-Reservierung). Tjorben hat in mehreren Sessions explizit geantwortet: „entscheide selbst" oder „das ist deine Sache". Diese Mid-Run-Halts haben die Lauf-Zeit verlängert und Tjorben unnötig zur Verfügung gehalten.

**Diagnose:** Die Cowork-Anweisung v1.14 (cowork_anweisung_datenimports.md) hatte keinen klaren Autonomie-Rahmen definiert — Cowork interpretierte „bei Unsicherheit halten" zu weit. Was eine harte Spec-Lücke ist (z.B. unbekannter Sprach-Begriff) und was eine Workflow-Detail-Entscheidung ist (z.B. Batch-Splitting), war operativ unklar.

**Entscheidung:** Cowork hat **Autonomie-Hoheit für Workflow-Entscheidungen**. Workflow-Details werden eigenständig entschieden, ohne User-Frage, und im Lauf-Bericht dokumentiert. STOPP-Trigger sind explizit aufgelistet — alles andere wird autonom durchgeführt.

**STOPP-Trigger (verpflichtend, alle anderen Fälle: autonom):**

1. **Fehlende Pflicht-Daten:** Lieferant nicht im Mapping, Pflichtfeld im Mapping null, kritisches Datenfeld vom Input fehlend (Material, Preise, Farbe).
2. **Unbekannte Sprach-Begriffe außerhalb Lookup:** Begriff nicht in SPEC_KONSTANTEN.md Sektion 6 (Produkt-Substantiv-Tabelle oder Farb-Tabelle). Niemals raten (AP8).
3. **Goldstandard-Abweichungen:** Strukturelle Abweichung von den 3 Pilot-Artikeln (Hekate Bodysuit, Arachne Bottom Teal, Savanna Original Top) ohne Lieferanten-Mapping-Eintrag.
4. **Mapping-null-Pflichtfelder:** Pflichtfelder im Mapping mit null-Wert ohne Default-Fallback.
5. **Drift-Verdacht:** Wenn Tjorben oder ein Trigger-Wortlaut nahelegt, dass sich Mapping/Schema geändert hat.

**Autonom (ohne User-Frage):**
- Batch-Splitting bei großen Lieferungen (E83 — Pre-Run Scope-Analyse)
- Token-Budget-Reservierung pro Stage
- Stage-Reihenfolge bei parallelisierbaren Stages
- Cross-Selling-Stage-Aktivierung (greift automatisch bei ≥2 Artikeln in der Lieferung mit gleichem Modell-Stamm)
- Wahl zwischen `requests` und `urllib` in Sandbox-Code
- Lokale Sub-Folder-Anlage im Workspace
- Wiederhol-Versuche bei transienten Drive-Fetch-Fehlern (max 2 Versuche, dann harter Fail)

**Konsequenz:**
- Im Lauf-Bericht **explizit dokumentieren**, welche autonomen Workflow-Entscheidungen Cowork getroffen hat
- Bei Verstoß (User-Frage zu Workflow-Detail): Self-Check-Punkt-Fail (nicht im 16-Punkte-Self-Check, aber im Cowork-Custom-Instructions-Style-Check)

**Validiert:** Live-Trial Batch 1+2 (2026-05-17) — Cowork hat autonom Batch-Splitting für 21 Modelle entschieden, im Bericht dokumentiert. Tjorben musste 0 Workflow-Fragen beantworten.

**Cross-Reference:**
- `cowork_anweisung_datenimports.md` v1.15 Sektion 4 (STOPP-Trigger-Liste)
- `cowork_anweisung_datenimports.md` v1.15 Sektion 12 (was Cowork DARF / NICHT DARF)
- `cowork_custom_instructions.md` v1.15 (Style-Check „autonom entscheiden, dokumentieren, nicht fragen")

---

**E82 — Stil-Verschärfung — Doppelpunkt-Verbot und Meta-Einleitungs-Verbot.**
*Stand:* 2026-05-17.

**Trigger:** Im Live-Trial Batch 1 Attribute-Generation am 2026-05-17 vormittags hat Cowork in mehreren Artikeldetails-Attributen Doppelpunkte in Taglines und im Fließtext gesetzt:
- Tagline: `<h2>Material: Mesh-Velvet</h2>` (statt z.B. `<h2>Mesh-Velvet Statement-Piece</h2>`)
- Fließtext: „Die Maße: Modellgröße 1,75m, Tragehöhe Hüfte..." (statt direkt: „Modellgröße 1,75m...")
- Sub-Header: „Die Pflege:" als Sub-Header vor Pflegehinweisen

Tjorben hat im Review beanstandet: „liest sich wie Spec-Datenblatt, nicht wie polesportshop". Doppelpunkte in Taglines und Meta-Einleitungs-Sätze („Die Maße:", „Die Pflege:", „Die Features:") wirken katalog-haft und brechen den E74-aspirational-Stil, der ab v1.13 etabliert war.

**Diagnose:** Die E22-Stilregeln (Em-Dash-Verbot, H1-Verbot) hatten Doppelpunkte explizit nicht abgedeckt. Cowork interpretierte Doppelpunkt als neutralen Satzzeichen und nutzte ihn häufig in strukturierenden Wendungen, ohne zu erkennen, dass er den aspirational Hook killt.

**Entscheidung:** Verschärfung der E22-Stilregeln. Em-Dash bleibt verboten (E22). NEU:

1. **Doppelpunkte in `<h2>`-Taglines verboten.** Tagline muss ein eigenständiger sprachlicher Hook sein, kein Spec-Label.
   - Schlecht: `<h2>Material: Mesh</h2>`
   - Gut: `<h2>Mesh-Material mit Stretch-Comfort</h2>` oder `<h2>Wenn Mesh auf Streetwear trifft</h2>`

2. **Doppelpunkte im Fließtext verboten** (außer in echten Aufzählungen mit nachfolgender Liste).
   - Schlecht: „Du brauchst: Stretch, Halt, Statement"
   - Gut: „Du brauchst Stretch, Halt, Statement" oder als prose: „Stretch trifft auf Halt und Statement-Optik"

3. **Meta-Einleitungs-Sätze verboten:** „Die Maße:", „Die Pflege:", „Die Features:", „Die Anwendung:". Direkt mit dem Inhalt beginnen.
   - Schlecht: `<h5 class="bold">Die Maße:</h5><p>Modellgröße 1,75m...</p>`
   - Gut: `<p>Auf 1,75m getragen, Tragehöhe an der Hüfte...</p>`

**Konsequenz:**
- Self-Check Punkt 13 wird erweitert um E82-Check: Tagline ohne Doppelpunkt? Fließtext ohne Meta-Einleitungs-Sätze?
- Pre-Output-Validierung in Stage 6 prüft alle Attribut-HTML-Strings auf das Pattern `:` in `<h2>...</h2>` und auf „Die X:"-Anfangsmuster.
- Cowork-Custom-Instructions wird um E82-Stilregel ergänzt (Style-Check „Doppelpunkt verboten in Taglines/Fließtext").

**Validiert:** Live-Trial Batch 2 (2026-05-17 nachmittags) mit E82-Verschärfung — Attribute-CSV hatte keine Doppelpunkt-Verstöße in Taglines, keine Meta-Einleitungs-Sätze, Tjorben hat den Stil als „endlich nicht mehr katalog-haft" abgenommen.

**Cross-Reference:**
- `cowork_anweisung_datenimports.md` v1.15 Sektion 5.5 (Stil-Briefing E82)
- `SPEC_KONSTANTEN.md` v1.15 Sektion 11 (Stil-Modus pro Attribut)
- `WAWI-IMPORT-WISSEN.md` v1.15 Sektion 6 (Attribute-Stolperfallen)

---

**E83 — Pre-Run Scope-Analyse als Stage 0.5.**
*Stand:* 2026-05-17.

**Trigger:** Im Live-Trial Batch 1 hatte Cowork ohne Vorab-Schätzung des Lauf-Volumens begonnen und ist nach 7 Modellen (von geplanten 10) in einen Token-Limit-Bereich gelaufen. Mid-Run-Abort wäre teuer gewesen, weil bereits 4 CSVs partiell geschrieben waren. Tjorben musste Cowork mit „weiter, splitte selbst" anstoßen, und Cowork hat dann ad-hoc Batch-Splitting nachgerüstet.

**Diagnose:** Die v1.14-Pipeline-Spec hatte keine Stage 0.5 für Volumen-Schätzung. Cowork startete direkt mit Stage 1 (Input erkennen) und stieß erst in späten Stages auf Token-Begrenzungen. Eine Pre-Run-Analyse hätte das Batch-Splitting vor Stage 1 entschieden, nicht reaktiv mittendrin.

**Entscheidung:** **Stage 0.5: Pre-Run Scope-Analyse** wird vor Stage 1 eingeführt. Cowork schätzt:

- **Anzahl Modelle × durchschnittliche Größen pro Modell × Multi-Kategorie-Faktor 2** → Stammdaten-Zeilen
- **Anzahl Modelle × 5 Sprachen** → Variationen-Zeilen
- **Anzahl Artikel (Vater + Kinder) × Anzahl Merkmale pro Artikel** → Merkmale-Zeilen
- **Anzahl Artikel × Anzahl Attribute (6-7) × 5 Sprachen** → Attribute-Zeilen
- **Cross-Selling: Modelle pro Modell-Stamm × bidirektional × 5 Kinder-Replikation × 2 Gruppen** → CSV-Zeilen (E80-Erweiterung v1.15)

**Token-Schätzung (Heuristik):**
- ~2-3K Tokens pro Modell für Stammdaten/Variationen/Merkmale
- ~8-12K Tokens pro Modell für Attribute (5 Sprachen, je 6 Attribute)
- Plus Cross-Selling-CSV-Generierung (deutlich kleiner, ~10K pro Lauf)

**Batch-Schwelle: 120K Tokens.** Wenn Schätzung >120K, autonom in Batches splitten.

**Output Stage 0.5:** Sektion „Pre-Run Scope-Analyse" im Lauf-Bericht:
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

**Konsequenz:**
- Cowork läuft nie mehr in Mid-Run-Token-Limits ohne Pre-Warning
- Batch-Splitting ist vor Stage 1 entschieden, nicht reaktiv
- Lauf-Bericht enthält Audit-Spur der Pre-Run-Schätzung (Tjorben kann Heuristik kalibrieren)

**Validiert:** Live-Trial Batch 2 (2026-05-17 nachmittags, 11 Modelle) — Cowork hat in Stage 0.5 Single-Batch-Lauf geschätzt (~95K Tokens), ist im Endeffekt bei ~88K Tokens gelandet (Schätzung gut), kein Batch-Splitting nötig.

**Cross-Reference:**
- `cowork_anweisung_datenimports.md` v1.15 Sektion 4 (Stage 0.5)
- `run_brief_daten.md` v1.15 (Stage-Übersicht-Tabelle)
- `BACKLOG.md` v1.15 B53 (Skalierungs-Validierung Batches >15 Modelle)

---

**E84 — Familien-erhaltende Split-Regel.**
*Stand:* 2026-05-17.

**Trigger:** Im hypothetischen 2-Batch-Szenario für die 21-Modell-Lieferung am 2026-05-17 hätte ein naiver Batch-Cut bei „Batch 1: Modelle 1-10, Batch 2: Modelle 11-21" die Arachne-Outfit-Pair-Familie zerschnitten: Arachne-Top-Black wäre in Batch 1 gelandet, Arachne-Bottom-Black in Batch 2. Cross-Selling-Stage 5.8 in Batch 1 hätte dann „Vervollständige Dein Outfit"-Beziehung Top↔Bottom **nicht finden können**, weil Bottom in Batch 1 nicht im Scope ist.

**Diagnose:** Batch-Splitting ohne Familien-Awareness produziert leise Cross-Selling-Lücken — die Beziehungen werden in keinem Batch geschrieben, weil jeder Batch nur Teilmenge sieht. Bei Re-Import erscheint Anzeige unvollständig im Shop, und es ist schwer zu debuggen, weil keine Fehlermeldung kommt.

**Entscheidung:** **Outfit-Pair-Familien werden niemals über Batches gesplittet.** Wenn ein Outfit-Paar (gleicher Modell-Stamm-Schlüssel `(modell_basis, farbe_im_namen)`, Top + Bottom) in zwei verschiedenen Batches landen würde, wird der Batch-Cut so verschoben, dass die Familie zusammen bleibt.

**Algorithmus:**
1. Cowork identifiziert alle Outfit-Pair-Familien in der Lieferung (z.B. Arachne-Black: Top + Bottom).
2. Beim Batch-Splitting werden Familien als atomare Einheit behandelt — nie über Batch-Cuts geteilt.
3. Wenn ein Batch dadurch das Token-Limit überschreitet (selten), wird der Batch-Cut entsprechend verschoben oder die Familie in den nächsten Batch geschoben.

**Cross-Selling-Stage-Sonderregel:**
- Cross-Selling-Stage 5.8 läuft im **letzten Batch**.
- Im letzten Batch lädt Cowork den vollen Lieferanten-Datensatz neu (oder hält ihn batch-übergreifend gecacht), damit Cross-Selling-Stage alle Familien aus allen Batches sieht.
- Cross-Selling-CSV wird nur einmal pro Lauf geschrieben — im letzten Batch.

**Konsequenz:**
- Keine Cross-Selling-Lücken bei Multi-Batch-Läufen
- Etwas weniger gleichmäßige Batch-Größen, dafür semantische Integrität
- Wenn eine Outfit-Pair-Familie selbst >120K Tokens braucht (theoretisch bei >40 Größen pro Vater), wird die Schwelle dynamisch erhöht (E81-Autonomie) und im Bericht vermerkt

**Validiert:** Live-Trial Batch 1+2 (2026-05-17) — Batch-Splitting wurde nicht aktiv ausgelöst (beide Batches innerhalb des Single-Batch-Limits), aber E84 wurde als Spec dokumentiert und in der nächsten skalierten Lieferung (>20 Modelle) als erstes geprüft.

**Cross-Reference:**
- `cowork_anweisung_datenimports.md` v1.15 Sektion 4 (Stage 0.5 + E84)
- `BACKLOG.md` v1.15 B53 (Skalierungs-Validierung — E84 wird beim ersten Multi-Batch-Lauf produktiv erprobt)
