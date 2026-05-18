# ENTSCHEIDUNGS-LOG-STIL-CONTENT-B

**Cluster:** Stil-Schliff, Brand-Identität, Cross-Selling (Teil B)

**Stand:** v1.17, 2026-05-17

**Bezug:** Dieser Cluster ist Teil des Splits der ursprünglichen `ENTSCHEIDUNGS-LOG.md` (v1.16, 165 KB → 6 Themen-Cluster ≤ 40 KB). Historische / abgelöste Einträge liegen weiterhin in `ENTSCHEIDUNGS-LOG-ARCHIV.md`. Cross-Cluster-Referenzen über E-Nummer; der Master-Index mit allen E-Nummern → Cluster-File-Zuordnung liegt in `SPEC_KONSTANTEN.md` unter `ENTSCHEIDUNGSLOG_E_NUMMER_INDEX`.

---

## Index

- **E53** — Eigene polesportshop-Stilidentität: Pole Junkie als Reduktion-Vorbild, polesportshop.de-DNA als Bestand
- **E71** — PO-Nummer komplett aus der Daten-Pipeline raus
- **E74** — Attribute-Stil-Pivot: Zielgruppe Frauen 25-35 fashionbegeistert Pole Dance, mehr Esprit und Verkaufsförderung
- **E75** — Anti-Confusion-Note: E57-Doppelzeilen sind kein Bug, sondern bewusstes Pattern + WaWi-Vorlagen-Setting-Pflicht
- **E76** — „Bottom" im deutschen Freitext verboten, immer „Shorts" verwenden
- **E77** — Anti-Plagiarism / Originalitäts-Pflicht schärfen + neuer Self-Check-Punkt 13
- **E78** — `material_and_care` clean & funktional, zwei klare Paragraphen
- **E79** — Neue HotCakes-Brand-Story als Evergreen mit Gründerinnen-Persönlichkeit
- **E80** — Cross-Selling-Architektur als 5. CSV-Output: „Vervollständige Dein Outfit" + „Ähnliche Artikel"
- **E80** — Erweiterung (2026-05-17, Live-Trial Batch 1+2 Erkenntnisse)

---

**E53 — Eigene polesportshop-Stilidentität: Pole Junkie als Reduktion-Vorbild, polesportshop.de-DNA als Bestand.**
*Stand:* 2026-05-15 Abend. Bezug: E22, E49.

*Warum:* Cowork hat im 3-Modell-Batch HTML-Artikeldetails geliefert die zu pathos-lastig waren („verleiht dir verführerischen Look", „atemberaubend"). Tjorben will reduzierte Sprache für Frauen-Zielgruppe, übersichtliche Feature-Auflistung, Pole-Junkie als Reduktions-Vorbild — aber **keine Copy-Paste-Identität**, sondern eine eigene polesportshop-Identität die auf der Bestand-DNA aufbaut.

*Stil-Briefing (in `cowork_anweisung_datenimports.md` v1.8 Sektion 5.5 verankert):*

**polesportshop.de-DNA (aus aktuellen Texten der Kategorie-Seiten):**
- Du-Form, konsequent
- Funktional zuerst: Halt, Grip, Bewegungsfreiheit, Hautkontakt
- Frauen direkt angesprochen, keine objektifizierende Sprache
- Performance-Vokabular: „sitzt, performt", „bring deine Performance aufs nächste Level"
- Selbstbewusstseins-Sprache, ohne Pathos
- Sport-Funktionalität vor Mode-Statement

**Pole-Junkie-Inspiration (gemäß E49 zulässig):**
- Reduktion: kurze Sätze, wenig Adjektive
- Konkret: Material, Schnitt, Anlass, statt vage Adjektive
- Keine Hard-Sell-Pathos

**Synthese — eigene polesportshop-Identität:**
- polesportshop-Funktionalität + Pole-Junkie-Reduktion
- Max 2-3 Sätze Fließtext pro Artikel
- `<ul class="check">` mit 3-5 Bullet-Features in einfacher Sprache
- Material/Schnitt-konkret statt „sexy/verführerisch"

**Verbotene Konstrukte:**
- `<strong>` HTML-Tag (Tjorben-Direktive 2026-05-15)
- Adjektive wie „sexy", „verführerisch", „aufreizend", „provokant" — funktional, nicht objektifizierend
- Em-Dashes (—) im Fließtext, ersetzen mit `,` oder `:`
- Anglizismen eingedeutscht (E22 unverändert: „Polewear" bleibt, „Pole Dance" bleibt)
- Pathos-Adjektiv-Kaskaden („atemberaubend, einzigartig, exklusiv")

**Beispiel-Templates:**

```html
<!-- ANTI-PATTERN (was wir nicht wollen): -->
<h2>Atemberaubender Mesh-Bodysuit für sexy Auftritte</h2>
<p>Dieser einzigartige, verführerische Bodysuit mit Marmor-Print verleiht
dir einen aufreizenden Look auf der Stange...</p>

<!-- POLESPORTSHOP-STIL (was wir wollen): -->
<h2>Marble-Print Mesh-Bodysuit mit Athletic-Back</h2>
<p>Mesh-Material für Hautkontakt am ganzen Körper. Tiefer Ausschnitt vorn
und offener Rücken für volle Bewegungsfreiheit an der Stange.</p>
<ul class="check">
  <li>Mesh-Stoff mit Marmor-Print</li>
  <li>Tiefer V-Ausschnitt vorn</li>
  <li>Open-Back-Design für Schulter-Mobilität</li>
  <li>Bodysuit-Schnitt: hält ohne zu verrutschen</li>
</ul>
```

*Pole-Junkie als Stil-Quelle nutzen (operativ):*
- Bei Crawl-Modus B kann Cowork Pole-Junkie-Produktseiten für denselben Artikel oder ähnliche Modelle aufrufen (E49-Direktive deckt das)
- Aus dem Pole-Junkie-Text die **Reduktions-Struktur** ableiten (welche Features werden genannt, wie kurz, in welcher Reihenfolge)
- **NIE Copy-Paste** — eigene Formulierung in polesportshop-DNA
- Im Bericht kurz vermerken: „Stil-Inspiration: Pole-Junkie-Eintrag <url>"

*Verworfen:*
- *Pole Junkie 1:1 als Identität übernehmen:* Tjorben hat ausdrücklich „eigene Identität" gefordert.
- *Hard-Sell-Marketing-Stil:* widerspricht polesportshop-Bestands-DNA und Zielgruppen-Tonalität.
- *`<strong>`-Tag für Hervorhebung:* Tjorben-Direktive 2026-05-15.

---

**E71 — PO-Nummer komplett aus der Daten-Pipeline raus.**
*Stand:* 2026-05-16. Bezug: heutiger Baseline-Lauf `run_2026-05-16_1928_hotcakes.md` Sektion 9, E54 (Schema append-only), E36 (Vorlagen-Defaults für Lieferantenblock).

*Warum:* Im Baseline-Lauf hat Cowork die PO `BE20261014195` korrekt als Nicht-Schema-Feld behandelt — das 48-Spalten-Schema ist append-only (AP4), spontane Spalten-Erweiterung ist verboten. Cowork hat die PO als „setzt Tjorben in der Ameise-Vorlage" markiert (Reiter Lieferanteneinstellungen → Bestellnummer-Feld), analog zu Währung (E36). Konsequente Folgerung: wenn die PO Vorlagen-Default ist, ist sie im Trigger redundant und in der Daten-Pipeline irrelevant. Schema-Append (Spalte 49 „Bestellnummer Lieferant") wurde von Tjorben ausdrücklich verworfen.

*Entscheidung:*
- PO-Nummer ist **nicht** Teil des CSV-Schemas, nicht in den Pipeline-Files, nicht im Trigger-Template.
- PO wird pro Lieferung **in der Ameise-Vorlage** als Default gesetzt (User-Konvention, kein Cowork-Schritt). Tjorben pflegt das einmalig vor dem Import.
- `run_brief_daten.md`, `cowork_anweisung_datenimports.md`, `cowork_custom_instructions.md` werden um jeden PO-Verweis bereinigt. Trigger-Template enthält keine PO-Zeile mehr.

*Konsequenzen:*
- Kein neuer Drift-Pfad: PO lebt nur in WaWi.
- Trigger werden kürzer und Lieferanten-agnostisch.
- Beim Onboarding neuer Lieferanten muss Tjorben das PO-Feld in der Stammdaten-Vorlage entweder fix befüllen oder beim Import-Vorgang setzen — analog zu Währung. Im Mapping kein neues Feld nötig.

*Verworfen:*
- *Spalte 49 „Bestellnummer Lieferant":* würde Schema-Append nach E54 erfordern, jeder Lieferanten-Lauf bräuchte trotzdem die PO-Eingabe — kein Mehrwert gegenüber Vorlagen-Default.
- *PO im Mapping pro Lieferant cachen:* PO ändert sich pro Lieferung, nicht pro Lieferant — wäre falscher Cache-Ort.

---

**E74 — Attribute-Stil-Pivot: Zielgruppe Frauen 25-35 fashionbegeistert Pole Dance, mehr Esprit und Verkaufsförderung.**
*Stand:* 2026-05-16. Bezug: E53 (Stilidentität 2026-05-15, „warm-funktional, sachlich-positiv"), E22 (HTML/Stil-Konventionen), Charter Prinzip 7 (Markenstimme).

*Warum:* Nach dem Baseline-Lauf bewertete Tjorben den Attribute-Stil als „zu funktional geworden". Die aktuelle E53-Tonalität („warm-funktional, sachlich-positiv, kein Hard-Sell, keine Superlative-Schreierei") war als Schutz vor Marketing-Schreierei gedacht — hat aber inzwischen ins Spec-Datenblatt-Register gekippt. Zielgruppe ist nicht Spec-Käufer-Männer, sondern fashionbegeisterte Frauen 25-35, die Pole Dance lieben. Die wollen aspirational angesprochen werden, nicht ingenieurssachlich.

*Entscheidung — neue Stil-Tonalität für `artikeldetails`, `markentext`, `material_and_care`, `size_and_fit`:*

**Zielgruppe-Definition:** Frauen 25-35, fashionbegeistert, Pole-Dance-Performer oder -Lifestyle-Anhängerinnen. Erwarten Outfits, die im Studio glänzen UND im Alltag funktionieren.

**Tonalität:** Warm, aspirational, mit Esprit. Du-Form. Verkaufsförderlich ohne Schreierei. Funktionalität bleibt erhalten, aber als zweite Stimme nach dem aspirational Hook — kein Spec-Datenblatt-Ton.

**Erlaubt (NEU mit E74):**
- Wohl gewählte starke Adjektive („verlängert optisch die Beine", „der mit dir mitatmet")
- Kleine emotionale Anker („für die Days, an denen du dich besonders sehen lassen willst")
- Fashion-Vokabular („Statement-Piece", „Wardrobe Essential", „geht von Studio zu Brunch")
- Pole-Insider-Sprache („Floor Work", „Climb", „Grip", „Aerial Hoop") — zeigt: wir kennen die Szene
- Sinnliche Wendungen mit Maß („Stoff, der sich anschmiegt wie eine zweite Haut")

**Verboten (bleibt aus E53):**
- Schreierei-Superlative („DAS BESTE TOP!")
- Marketing-Klischees („Lass deine Träume wahr werden")
- Hashtags, Emojis
- Werbe-Imperative („shop now", „jetzt kaufen")
- Sexistische Anbiederung oder Objektifizierung

**Werte-Anker (bleibt aus E53, geschärft):**
- Nachhaltigkeit/Vegan/Tierversuchsfrei wo zutreffend
- Body Positivity & Empowerment
- Pole als Sport UND Lifestyle, nicht nur „Sportgerät"

**Beispiel zur Kalibrierung (Peonies Top in Nude):**
- *Alt (zu funktional):* „Mit hohem Beinausschnitt für mehr Bewegungsfreiheit und doppelt gefüttertem Bund für besseren Halt."
- *Neu (aspirational + funktional):* „Hoher Beinausschnitt verlängert optisch die Beine. Der doppelt gefütterte Bund sitzt, egal wie viel du dich bewegst — beim Floor Work, beim Climb, beim Brunch danach."

*Spec-Verankerung:*
- `cowork_anweisung_datenimports.md` Sektion 5.5 wird vollständig neu geschrieben (Vollumbau dieser Sektion via `create_file`).
- `run_brief_daten.md` Stil-Kurz-Sektion analog angepasst.
- Diese E74-Sektion im LOG ist die kanonische Begründung.

*Konsequenzen:*
- Polesportshop bekommt eine erwachsene, aspirational Markenstimme zurück.
- Cowork muss bei jeder Sprache aktiv aspirational-fashion arbeiten (nicht nur DE), siehe E73.
- Erster Bewertungspunkt nach dem nächsten Trial-End-to-End-Run: passt die neue Stimme zur Zielgruppe? Iteration nach Shop-Review möglich.

*Verworfen:*
- *Zwei separate Tonalitäten je nach Artikelart (Sport-Bottom vs. Bodysuit):* würde Spec-Komplexität ohne Mehrwert erhöhen. Eine Stimme über alle Artikel.
- *Tonalität pro Lieferant differenzieren:* HotCakes wäre dann anders als POLE ADDICT. Auch hier: Polesportshop hat eine Stimme, nicht zehn.

---

**E75 — Anti-Confusion-Note: E57-Doppelzeilen sind kein Bug, sondern bewusstes Pattern + WaWi-Vorlagen-Setting-Pflicht.**
*Stand:* 2026-05-16. Bezug: E57 (Multi-Kategorie via Doppelzeilen, 5 Forum-Threads + Re-Import validiert), heutige Falsch-Diagnose im Klärungs-Chat (Claude-Selbstkorrektur dokumentiert).

*Warum:* Beim ersten WaWi-Import-Versuch nach dem Baseline-Lauf 2026-05-16 las Tjorben „doppelte Größen" als Symptom. Claude diagnostizierte voreilig die Doppelzeilen-Architektur als Spec-Bug und bot eine korrigierte CSV mit halbierter Zeilenzahl (29 statt 58). Beim Spec-Cross-Check stellte sich heraus: das Pattern ist E57, Forum-recherchiert, validiert. Das tatsächliche Symptom war ein WaWi-Setting-Issue (nicht reproduzierbar, da Tjorbens Vorlagen-Setting bei Re-Prüfung korrekt war — der Goldstandard `1_Stammdaten_HotCakes_2026-05-16.csv` hat ebenfalls Doppelzeilen und wurde sauber importiert).

Die Falsch-Diagnose war ein klassisches Antibody-Failure: ungeprüfte Hypothese kombiniert mit fehlendem Spec-Cross-Check. Damit das nicht wieder passiert (von mir oder von Cowork in einem späteren Lauf), wird die Klarstellung an drei Stellen verankert.

*Entscheidung — Anti-Confusion-Note an drei Stellen einbauen:*

1. **`WAWI-IMPORT-WISSEN.md` Sektion zu Multi-Kategorie (E57):** ein expliziter Anti-Patterns-Block mit dem Wortlaut „Wenn jemand Doppelzeilen als Bug meldet: KEIN Spec-Eingriff. Erst prüfen: ist das Vorlagen-Setting `Kategorieverknüpfungen des Artikels aktualisieren = Neue Kategorien beim jeweiligen Artikel hinzuimportieren` gesetzt? Wenn nicht: Setting fixen, originale CSV nochmal importieren. Wenn ja und Bug bleibt: dann erst Architektur-Diskussion."

2. **`SPEC_KONSTANTEN.md` Self-Check Punkt 4:** Klarstellung am Rand der Regel-Zeile, dass die Doppelzeilen-Logik kein Bug ist, sondern E57.

3. **`BACKLOG.md` neue Anomalie A9 (archiviert):** „Falsch-Diagnose E57 als Bug, archiviert 2026-05-16 — siehe E75". Damit Future-Claude sieht: diese Diagnose wurde schon mal falsch geführt, hier ist die Klarstellung.

*Konsequenzen:*
- Spec bleibt unverändert (E57 ist korrekt).
- Drei Verankerungs-Punkte machen es Future-Claude und Cowork schwerer, denselben Fehler nochmal zu machen.
- Charter Prinzip 10 (kein Erfinden) wurde durch die Selbstkorrektur eingehalten — die Diagnose-Antibody-Failure wird transparent dokumentiert, nicht versteckt.
- Lehre für Klärungs-Chats: bei vermuteten Spec-Bugs zuerst die Spec-Cross-Check (grep nach dem Pattern in LOG / WAWI-IMPORT-WISSEN), bevor Fix-CSVs gebaut werden.

*Verworfen:*
- *A9 als aktive Anomalie führen:* die Anomalie ist gelöst (Spec ist korrekt, Anti-Confusion-Note verankert), nicht offen. Archiviert ist die richtige Schublade.
- *Falsch-Diagnose verschweigen:* Charter Prinzip 10 verlangt Transparenz. Lehre transparent gemacht, schützt zukünftige Iterationen.

---

**E76 — „Bottom" im deutschen Freitext verboten, immer „Shorts" verwenden.**
*Stand:* 2026-05-16. Bezug: E58 (Sprach-Lokalisierungs-Konvention), E74 (Stil-Pivot), Tjorben-Direktive nach Generalprobe-Review.

*Warum:* Im Generalprobe-Bericht 2026-05-16 (`run_2026-05-16_2022_hotcakes.md`) tauchte im deutschen `artikeldetails`-Text der Peonies-Bottom der Satz auf: „Diese **Bottom** ist nicht das Beiwerk zum Top". Cowork hatte „Bottom" als legitimen Anglizismus interpretiert — analog zu „Polewear", „Pole Dance", „Cheeky". Aber: „Pole Dance Shorts" ist für polesportshop ein zentrales SEO-Keyword. Jeder vermiedene „Shorts"-Treffer im deutschen Freitext kostet Such-Sichtbarkeit. „Bottom" als Begriff ist im deutschen Pole-Markt nicht etabliert (anders als die zuvor erlaubten Anglizismen).

*Entscheidung:*
- **Im deutschen Freitext (alle `artikeldetails`, `markentext`, `material_and_care`, `size_and_fit`, Meta-Description, etc.) gilt: „Shorts" statt „Bottom".** Hartcodierte Regel, keine Ausnahme.
- Analog „Top" bleibt „Top" auf Deutsch (das ist ja keine Übersetzung, sondern Standard-Deutsch).
- Im Strukturfeld (z.B. Spalte „Artikelname" → „HotCakes Shorts Peonies Nude") war's eh schon richtig durch E58. Diese Regel wirkt jetzt zusätzlich auf den HTML-Freitext.
- SPEC_KONSTANTEN Sektion 6 erhält eine neue Unter-Sektion „Hartkodierte DE-Konventionen" mit „Bottom→Shorts" als erster Eintrag.
- Stil-Briefing in `cowork_anweisung_datenimports.md` Sektion 5.5 und `run_brief_daten.md` Sektion 9 nehmen „Bottom" in die Verbots-Liste der Konstrukte auf.

*Konsequenzen:*
- Keine Treffer-Verluste mehr beim SEO-Keyword „Pole Dance Shorts" wegen „Bottom"-Synonymen.
- Cowork-Stilregel: bei DE-Texten zu Pole-Dance-Hosen immer „Shorts", auch wenn der Hersteller-Body „Bottom" sagt.
- EN/FR/IT/ES sind nicht betroffen — dort ist „Bottom" / „bas" / „bottom" als Pol-Standardbegriff OK.

*Verworfen:*
- *„Bottom" als deutscher Anglizismus erhalten:* würde den SEO-Schaden nicht beheben.
- *Globale Eindeutschungs-Regel auf alle Anglizismen ausdehnen:* würde „Polewear", „Pole Dance", „Grip", „Climb" mitfangen — die wollen wir aber als Insider-Vokabular behalten (E74). Punktuelle Regel pro Begriff.

---

**E77 — Anti-Plagiarism / Originalitäts-Pflicht schärfen + neuer Self-Check-Punkt 13.**
*Stand:* 2026-05-16. Bezug: E49 (Pole-Junkie-Inspiration, NIE Copy-Paste), E70 (Pole-Junkie-Cross-Reference auch für Features), E74 (Stil-Pivot), Charter-Prinzip 7 (Markenstimme), Tjorben-Direktive nach Generalprobe.

*Warum:* Bisherige Anti-Plagiarism-Regel war: „NIE Copy-Paste von Pole Junkie, eigene Formulierung in polesportshop-DNA" (E49). Die ist textuell stark, aber strukturell schwach — ein Cowork-Sub-Agent kann paraphrasieren oder Synonyme einsetzen, ohne im engen Sinn „Copy-Paste" zu machen, und trotzdem ist die Quelle erkennbar. Tjorbens Anforderung: Kunden sollen nicht denken, dass polesportshop bei Pole Junkie oder beim Hersteller kopiert hat. Die Stimme muss eindeutig polesportshop sein, nicht nur „nicht plagiiert".

*Entscheidung:*
- **Verschärfung der Anti-Plagiarism-Regel** in Sektion 5.5 (datenimports) und Sektion 9 (run_brief): „Lies Hersteller-Text, lies ggf. Pole-Junkie-Text — und schreib **komplett neu** in polesportshop-Sicht. Nicht paraphrasieren (anderes Wort, gleiche Satz-Struktur), nicht synonymisieren (gleicher Inhalt, andere Wörter), nicht umstellen (gleicher Inhalt, andere Reihenfolge). **Neu denken**: was würde polesportshop diesem Produkt sagen, wenn die Quellen nicht existierten?"
- **Neuer Self-Check Punkt 13 (Originalitäts-Check)** in SPEC_KONSTANTEN Sektion 9: für jeden generierten `artikeldetails`-Text prüft Cowork programmatisch oder textuell, ob Sätze strukturell oder lexikalisch zu nah an einer bekannten Quelle sind. Wenn ja: umschreiben. Konkret-prüfbar: keine wörtliche 5-Wörter-Sequenz aus Hersteller-Body übernommen, keine 1:1-Übernahme der Sub-Sätze-Reihenfolge des Hersteller-Bodys, keine Pole-Junkie-Tagline-Imitationen.
- Cross-Reference E70 bleibt erlaubt, aber mit dem Zusatz: die polesportshop-Stimme dominiert die abgeleitete Information. Pole Junkie liefert Struktur-Idee und Feature-Bestätigung, nicht Wording.

*Konsequenzen:*
- Cowork-Generierung wird leicht teurer (Token-Mehraufwand für „neu denken" statt „paraphrasieren"), aber das ist gewollt.
- Im Lauf-Bericht steht ab v1.14: Self-Check 13/13 statt 12/12 — Punkt 13 ist Originalitäts-Check.
- Bei Fail: Cowork umschreibt automatisch, falls strukturelle Plagiat-Indikatoren auftauchen. Im Lauf-Bericht dokumentiert.

*Verworfen:*
- *Pole-Junkie-Cross-Reference komplett deaktivieren:* würde E70-Pragmatik kippen. Pole Junkie ist legitime Feature-Verifikations-Quelle, nur das Wording darf nicht durchschimmern.
- *Externe Plagiat-API einsetzen:* zusätzliche Komplexität, kein Mehrwert über strukturellen Check hinaus.

---

**E78 — `material_and_care` clean & funktional, zwei klare Paragraphen.**
*Stand:* 2026-05-16. Bezug: E74 (Stil-Pivot für aspirational), Tjorben-Direktive nach Generalprobe.

*Warum:* Tjorben hat im Generalprobe-Review festgestellt, dass `material_and_care` mit dem allgemeinen E74-Stil-Pivot zu lebhaft / zu beschreibend wurde. Das ist falsch positioniert: `material_and_care` ist ein **regulatorisch-funktionales Feld** (EU-Textilkennzeichnungs-Pflicht erfordert die Stoffzusammensetzung) — kein Verkaufs-Text. Aspirational + Esprit gehört in `artikeldetails` und `markentext`, nicht hier. Funktionalität rein, fertig.

*Entscheidung — Aufbau `material_and_care` ab v1.14:*

**Paragraph 1: Stoffzusammensetzung.** Reine Material-Angabe in Prozent, nach EU-Textilkennzeichnungsverordnung-Konvention. Beispiel: `<p>85% Polyamid, 15% Elasthan.</p>` Kein beschreibender Text, kein Sales-Wording, keine sinnlichen Adjektive. Nur Fakten.

**Paragraph 2: Pflegehinweise.** Funktionale Aufzählung der Pflege-Symbole / -Anweisungen. Beispiel: `<p>Handwäsche bei 30°C, nicht bleichen, nicht in den Trockner, nicht bügeln, nicht chemisch reinigen.</p>` Bullet-Liste optional, aber nicht zwingend. Wieder: keine Beschreibungen, keine „der schonenden Pflege wegen sollten Sie..."-Sätze. Nur Anweisungen.

**Was hier verboten ist** (Abweichung vom E74-Stil-Pivot, der für `artikeldetails` etc. weiter gilt):
- Sinnliche Adjektive („zarte Pflege", „samtige Berührung")
- Verkaufsförderliche Hinweise („damit der Glanz erhalten bleibt")
- Beschreibende Begründungen („weil das Material besonders empfindlich ist")
- E74-Wendungen („geht von Studio zu Brunch") — hier komplett fehl am Platz

**Was bleibt:** Du-Form ist OK (z.B. „Wasche bei 30°C") oder förmliche Imperativ-Form („Bei 30°C waschen") — Cowork wählt eine Variante und hält sie pro Lieferant konsistent.

*Spec-Verankerung:*
- `cowork_anweisung_datenimports.md` Sektion 5.4 (Attribute) erhält einen Unter-Block „material_and_care: clean Pattern (E78)".
- `run_brief_daten.md` Sektion 12 (Attribute-Schemas) analog kurz.
- `SPEC_KONSTANTEN.md` Sektion 7 oder neue Sektion „Attribute-Stil-Unterschiede pro Feld" — `markentext` + `artikeldetails` = E74-aspirational, `material_and_care` + `size_and_fit` = clean/funktional.

*Konsequenzen:*
- Klarer Stil-Unterschied pro Attribut: aspirational für die Storytelling-Felder, clean für die regulatorischen.
- Cowork muss pro Attribut-Feld unterschiedlich „dosieren" — höhere Stil-Granularität.
- Beim Shop-Review: `material_and_care`-Block sollte wie eine Tabelle wirken, nicht wie ein Werbe-Text.

*Verworfen:*
- *`size_and_fit` mit `material_and_care` zusammenlegen:* sind unterschiedliche Aspekte (Größe/Passform vs. Material/Pflege), bleiben separat.
- *`size_and_fit` ebenfalls clean:* bleibt im E74-aspirational, weil Passform-Erläuterung Verkaufsthema ist („eng anliegend für freie Pole-Bewegung" hat Mehrwert).

---

**E79 — Neue HotCakes-Brand-Story als Evergreen mit Gründerinnen-Persönlichkeit.**
*Stand:* 2026-05-16. Bezug: E72 (Brand-Story-Caching pro Lieferant), Tjorben-Direktive nach Generalprobe-Review.

*Warum:* Die v1.13-Brand-Story für HotCakes hat im Generalprobe-Lauf ihren Zweck erfüllt (E72 funktioniert, 1:1 als `markentext` verwendet, kein E70 mehr). Aber im Shop-Review fiel auf: der Text ist nicht „evergreen" (er nennt Print-Serien wie Peonies, Hekate-Marble, Dark Roast — die wechseln, und der Text müsste mit jedem neuen Kollektions-Drop angepasst werden) und er hat zu wenig Persönlichkeit (Kunden sollen eine **Bindung** zur Marke aufbauen, nicht nur Marketing-Phrasen lesen). Recherche auf hotcakespolewear.com lieferte echte Brand-Substanz: Gründerinnen Maro, Plousia und Thomis (zwei professionelle Pole-Tänzerinnen + eine bekannte Mode-Designerin), gemeinsamer Hintergrund im Bühnen-Kostüm-Design, Vision „Originalität, Qualität, Klasse", Selbst-Beschreibung „From a dancer's mind to a dancer's body".

*Entscheidung:*

**Neue HotCakes-Brand-Story-Anforderungen:**
- **Evergreen:** keine Kollektions- oder Print-Serien-Erwähnungen (Peonies, Hekate, Dark Roast bleiben den `artikeldetails` vorbehalten, nicht der Brand-Story). Was die Marke ausmacht, nicht was sie aktuell verkauft.
- **Persönlichkeit:** die drei Gründerinnen als Stimme. „Von zwei Tänzerinnen und einer Designerin, die sich beim Kostüm-Schneidern für Pole-Shows kennen gelernt haben."
- **Bindung:** eine Geschichte, mit der sich die Zielgruppe (Frauen 25-35, fashionbegeistert, Pole) identifizieren kann. Nicht über die Marke reden, sondern die Welt der Marke öffnen.
- **Sprach-Pflicht (E73):** alle 5 Sprachen voll, eigene Tonalität pro Sprache.
- **Stil-Pflicht (E74):** aspirational + Esprit, keine Pathos-Adjektive, keine Marketing-Schreierei.
- **Anti-Plagiarism (E77):** komplett neue Formulierung, kein Paraphrasing der hotcakespolewear-About-Page.

**Pflege-Ort:** `lieferanten_mapping.yaml` Felder `brand_story_de/en/fr/it/es` für HotCakes in v1.14 komplett neu.

*Konsequenzen:*
- Brand-Story für HotCakes wird einmalig kuratiert und bleibt stabil über Folgelieferungen.
- Pattern für künftige Lieferanten: beim Onboarding wird die Gründerinnen-/Marken-Story-Quelle aktiv recherchiert (About-Page, Interviews, Presse), nicht generisch generiert.
- Verfeinert die E72-Pflege-Konvention: nicht „irgendeine Brand-Story" sondern „evergreen Brand-Story mit echter Substanz".

*Verworfen:*
- *Generische Brand-Story behalten:* würde den E72-Pivot weiter verwässern.
- *Brand-Story dynamisch aus Crawl ableiten:* fragil, Quelle ändert sich plötzlich, manuell kuratiert bleibt robuster.

---

**E80 — Cross-Selling-Architektur als 5. CSV-Output: „Vervollständige Dein Outfit" + „Ähnliche Artikel".**
*Stand:* 2026-05-16. Bezug: Tjorben-Direktive nach Generalprobe (Screenshot der WaWi-Cross-Selling-Gruppen-Maske), JTL-Ameise Cross-Selling-Import-Schema.

*Warum:* polesportshop nutzt im Shop zwei Cross-Selling-Gruppen, die in WaWi vor-existieren: „Vervollständige Dein Outfit" (Top-Bottom-Pairs in gleicher Farbe) und „Ähnliche Artikel" (gleiches Modell in anderen Farben). Bis v1.13 wurden diese manuell pro Artikel in WaWi gepflegt. Bei steigendem Lieferanten-Volumen (heute 5 Modelle, Produktions-Run mit 14 weiteren, später dutzende pro Lieferung) wird die manuelle Pflege zum Engpass. Die Pipeline soll die Beziehungen automatisch erkennen und als 5. CSV-Output mitliefern.

JTL-Ameise hat einen eigenen Import-Typ „Cross-Selling-Artikel" mit klar definiertem 3-Spalten-Schema (recherchiert 2026-05-16 via JTL-Guide):

```
Artikelnummer; Artikelnummer Cross-Seller; Cross-Selling-Gruppe
```

Eine Zeile pro Beziehung. Cross-Selling-Gruppen müssen vorab in WaWi existieren — sind sie bei polesportshop (Screenshot 2026-05-16). Beim Import nutzt Cowork eine neue Ameise-Vorlage `{Lieferant}_5_CrossSelling` (Naming-Konvention E29, fortlaufend nach 1_Stammdaten / 2_Variationen / 3_Attribute / 4_Merkmale; bestehende Legacy-Slots im jeweiligen Mapping ggf. zu beachten).

*Entscheidung — Architektur:*

**1. Neue 5. CSV pro Lauf:** `5_CrossSelling_{lieferant_kuerzel}_{datum}.csv`
   - Encoding: UTF-8 mit BOM
   - Trennzeichen: `;`
   - Quote: `MINIMAL`
   - Zeilenende: CRLF
   - 3 Spalten: `Artikelnummer; Artikelnummer Cross-Seller; Cross-Selling-Gruppe`

**2. Algorithmus pro Lauf:**
   - Cowork lädt **vollen Shopify-Datensatz** (z.B. alle 124 HotCakes-Produkte aus `/products.json`), nicht nur die Trigger-Modelle. Diese Erweiterung wird in Stage 1 (Crawl) festgehalten.
   - Pro Vater-Artikel der Lieferung (= Trigger-Modelle): identifiziere
     - **Modell-Familie** (z.B. „Peonies Top", „Peonies Bottom", „Savanna Top")
     - **Farb-Variante** (z.B. „Nude", „Mauve", „Sky")
     - **Typ** (Top / Bottom / Bodysuit)
   - Berechne Beziehungen aus dem vollen Datensatz:
     - **„Vervollständige Dein Outfit":** gleicher Modell-Stamm + gegensätzlicher Typ (Top↔Bottom) + gleiche Farbe → eine Zeile pro Richtung (A→B + B→A)
     - **„Ähnliche Artikel":** gleicher Modell-Stamm + gleicher Typ + andere Farbe → eine Zeile pro Richtung
   - Nur Vater-Artikelnummern, **keine Kind-Artikelnummern** mit Größen-Suffix.
   - Symmetrie: jede Beziehung beidseitig zur Sicherheit für korrekte Cross-Selling-Anzeige im Shop.

**3. Neue Stage in der Pipeline:** Stage 5.6 — Cross-Selling-Generierung (vor Stage 6 Self-Check, weil der Self-Check die 5. CSV mitprüfen muss).

**4. Neue Self-Check-Punkte ab v1.14:**
   - Punkt 14: Cross-Selling 3-Spalten-Schema korrekt
   - Punkt 15: nur Vater-Artikelnummern in den Cross-Selling-Beziehungen (keine `-001`, `-002` etc.)
   - Punkt 16: jede Beziehung beidseitig (A→B + B→A)

(Plus Punkt 13 aus E77 — Originalitäts-Check. Punkte werden also 12 → 16 ab v1.14.)

**5. Neue Ameise-Vorlage pro Lieferant:** `cross_selling: "HotCakes Polewear_5_CrossSelling"` im Mapping, vor Trial-End-to-End-Run von Tjorben in WaWi anzulegen. Spalten-Zuordnung in Vorlage: `Artikelnummer` (Identifizierungsspalte), `Artikelnummer Cross-Seller` (Artikel-IDs-Cross-Selling-Artikel), `Cross-Selling-Gruppe` (Cross-Selling).

**6. Mapping-Schema-Erweiterung:** neues Feld `ameise_vorlagen.cross_selling` pro Lieferant (Pflichtfeld ab v1.14 — Cowork bricht ab und fragt nach wenn null und Cross-Selling-Generierung getriggert ist).

**7. Vorlagen-Anzahl pro Lieferant wächst von 4 auf 5.** Pre-Produktions-Hinweis-Konvention in Cowork-Custom-Instructions entsprechend anpassen.

*Konsequenzen:*
- Cross-Selling-Pflege wird vollautomatisiert — manuelle Stunden-Arbeit pro Lieferung entfällt.
- Volumen-Effekt: bei wachsenden Lieferanten-Sortimenten wachsen die Beziehungs-Zeilen quadratisch (n Farben × m Typen = n×(n-1)×m Beziehungs-Zeilen für „Ähnliche", plus Outfit-Pairs). Bei 124 HotCakes-Produkten ist das überschaubar, bei größeren Lieferanten Plan B: nur Beziehungen innerhalb der aktuellen Lieferung + bestehender WaWi-Artikel.
- Tjorbens Cross-Selling-Pflege im Shop wird konsistent und vollständig statt punktuell-manuell.
- Trial-Run-Erweiterung: nächste Generalprobe nutzt alle 19 Modelle der Rechnung #00034 (nicht nur 5), damit die SAVANNA-Familie mit 3 Farben (Mauve/Original/Sky) als echter „Ähnliche Artikel"-Test mit dabei ist.

*Verworfen:*
- *Cross-Selling pro Lauf-Kontext (nur die Trigger-Modelle berücksichtigen):* würde Beziehungen zu Artikeln verlieren, die nicht im aktuellen Trigger sind aber im Shop existieren. Voller Shopify-Datensatz ist nötig.
- *Cross-Selling-Beziehungen NUR in eine Richtung schreiben:* WaWi sollte das eigentlich bidirektional auflösen — zur Sicherheit beide Richtungen schreiben, falls die Bidirektionalität in einer WaWi-Version anders aufgelöst wird.
- *Kind-Artikelnummern auch in Cross-Selling aufnehmen:* würde Shop-Anzeige zerschießen (Kinder erscheinen nicht als eigenständige Cross-Selling-Empfehlung).
- *Cross-Selling als Spalte in Stammdaten-CSV statt 5. CSV:* JTL-Ameise hat einen dedizierten Import-Typ — passende Architektur ist eine eigene CSV.


---

**E80-Erweiterung (2026-05-17, Live-Trial Batch 1+2 Erkenntnisse).**

E80 hat sich in der ersten produktiven Anwendung (HotCakes Batch 1+2 am 2026-05-17) als grundsätzlich tragfähig erwiesen — die 5-CSV-Architektur lief beide Batches mit 16/16 Self-Check grün. Aus dem Lauf entstanden drei Erweiterungen, die hier als E80-Sub-Einträge angehängt werden, weil sie das gleiche Architektur-Element (Cross-Selling-CSV) verfeinern, nicht ersetzen.

### E80-Erweiterung 1: Cross-Selling auf Vater UND alle Kinder (Kinder-Replikation)

**Beobachtung Live-Trial Batch 1 (10 Modelle, 2026-05-17 vormittags):**
Cross-Selling-Anzeige im Shop greift nach dem Initial-Import zwar auf Vater-Artikeln (z.B. „Peonies Top Nude" zeigt „Peonies Bottom Nude" als Cross-Seller), aber **nicht auf den Kind-Artikel-Detailseiten** (Größen-Varianten). Der Shop zeigt auf der Detailseite einer Kind-Variante (z.B. „Peonies Top Nude S") keine Cross-Selling-Empfehlungen, obwohl der Vater eine Beziehung hat.

**Ursache:** WaWi-Cross-Selling-Zuweisung wirkt artikelnummer-spezifisch. JTL erbt Cross-Selling-Beziehungen **nicht implizit** von Vater zu Kindern — analog zum bekannten Erbungs-Verbot bei Merkmalen (E19), Attributen (E34) und Bildern (E46). Dieses Pattern ist konsistent mit JTL-Default-Architektur.

**Entscheidung:** Cross-Selling-CSV repliziert die linke Spalte (`Artikelnummer`) auf Vater **und alle Kind-IDs**. Rechte Spalte (`Artikelnummer Cross-Seller`) bleibt strikt Vater (Kind-Größen als Cross-Seller würde im Shop fragmentierte Empfehlungen erzeugen — „kaufe Peonies Bottom Nude S" statt „kaufe Peonies Bottom Nude").

**Konsequenz für Pipeline:**
- Pro bidirektionale Beziehung: statt 2 Zeilen jetzt **2 × (1 + N) Zeilen** bei N Größen pro Vater
- Beispiel HotCakes typische Outfit-Pair-Familie (5 Größen pro Vater): 12 Zeilen pro bidir. Beziehung statt 2
- Batch 2 (11 Modelle, 16 bidir. Beziehungen): **180 Zeilen** in der CSV statt 36 (Faktor 5)

**Validiert:** Batch 2 Import 2026-05-17 nachmittags lief mit dieser Mechanik durch, Cross-Selling-Anzeige funktioniert nun auf Vater- UND Kind-Detailseiten im Shop. Self-Check 15 (NEU v1.15) prüft das vor jedem CSV-Output.

### E80-Erweiterung 2: Modell-Stamm-Schlüssel inkludiert Farbe

**Beobachtung Live-Trial Batch 2 Iteration 1 (2026-05-17 mittags):**
Cross-Selling-CSV Iteration 1 enthielt **falsche Outfit-Pair-Zuweisungen**: „Arachne Top Black" wurde mit „Arachne Bottom Teal" als „Vervollständige Dein Outfit" gepaart. Im Shop führte das zu absurden Empfehlungen (Schwarz mit Türkis kombiniert). Cowork hatte den Modell-Stamm-Schlüssel als `(modell_basis)` = `"Arachne"` definiert, was alle Arachne-Modelle als gleiche Familie behandelte unabhängig von der Farbe.

**Diagnose:** Die ursprüngliche E80-Spezifikation (v1.14) hatte den Modell-Stamm-Schlüssel implizit nur als Modellname (z.B. „Arachne"), nicht als Modell+Farbe-Kombination. Outfit-Pair-Matching braucht aber Farb-Gleichheit, um sinnvolle Empfehlungen zu erzeugen.

**Entscheidung:** Modell-Stamm-Schlüssel ist `(modell_basis, farbe_im_namen)`. Beispiele:
- `("Arachne", "Black")` — Arachne-Schwarz-Familie (Top Black + Bottom Black)
- `("Arachne", "Teal")` — Arachne-Türkis-Familie
- `("Peonies", "Nude")` — Peonies-Nude-Familie

Bei „Vervollständige Dein Outfit"-Matching: Top und Bottom müssen denselben Schlüssel haben. Bei „Ähnliche Artikel"-Matching: gleicher `modell_basis`, anderer `farbe_im_namen`.

**Konsequenz:**
- Pro Modell + Farbe entsteht ein eigener Stamm-Cluster für Cross-Selling
- Multi-Farb-Modelle wie Arachne erzeugen N Stamm-Cluster (für N Farben)
- Outfit-Paarungen sind farb-treu

**Validiert:** Batch 2 Iteration 2 (2026-05-17 nachmittags) mit korrektem Schlüssel lief durch — alle 11 Modelle hatten farb-konsistente Outfit-Paarungen im Shop.

**Implementierungs-Hinweis:** Bei Modellen ohne explizite Farbe im Namen (z.B. „Savanna Original") wird `farbe_im_namen` aus dem Shopify-Tag oder einem Mapping-Override im Lieferanten-Mapping geholt. Wenn nicht eindeutig: STOPP + User-Frage (E81-Trigger 2).

### E80-Erweiterung 3: Cross-Selling-Family-Refresh als optionaler Trigger-Modus

**Anwendungsfall:** Wenn neue Schwester-Artikel zu einem bestehenden Modell-Stamm im Shop angelegt werden (z.B. eine neue Farbvariante eines bestehenden Modells), müssen die Cross-Selling-Beziehungen aktualisiert werden: alte „Ähnliche Artikel"-Beziehungen verweisen jetzt auf einen zusätzlichen Schwester-Artikel, der vorher nicht existierte.

**Beobachtung 2026-05-17:** Bei Tjorbens HotCakes-Bestand gibt es mehrere Modell-Stämme mit historischen Schwester-Artikeln, die noch nicht in der Cross-Selling-Tabelle abgebildet sind:
- Arachne: Tan und Cherry zusätzlich zu Black und Teal
- Savanna: Black, Skin, Emerald, Lime, Heat zusätzlich zu Original
- Peonies Bodysuit: skin-tones

Ein voller Re-Lauf der gesamten Daten-Pipeline (alle 4 Artikel-CSVs + Cross-Selling) für diese Schwester-Artikel ist überdimensioniert — die Artikel sind schon angelegt, nur die Cross-Selling-Beziehungen fehlen.

**Entscheidung:** Es gibt einen optionalen Trigger-Modus „Cross-Selling-Family-Refresh". Trigger-Beispiel:

> „Verarbeite Cross-Selling-Refresh für HotCakes, Modell-Stamm Arachne"

Cowork:
- skippt Stage 1-5.7 für CSVs 1-4
- lädt den vollen Lieferanten-Datensatz aus Shopify (oder Mapping-Lieferanten-Drive)
- führt **NUR Stage 5.8** für den gegebenen Modell-Stamm-Scope aus (alle Farben + Typen mit `modell_basis == "Arachne"`)
- generiert nur `5_CrossSelling_<LIEFERANT>_<DATUM>.csv` als einzige Output-Datei
- Im Lauf-Bericht explizit als „Cross-Selling-Family-Refresh-Lauf" markieren

**Konsequenz:**
- Kein Re-Import von Stammdaten/Variationen/Merkmale/Attribute nötig — die Schwester-Artikel sind schon im Shop
- Cross-Selling-Tabelle wird mit neuen Beziehungen aktualisiert (additiv, dank E80 v1.14 bidirektionaler Doppelschreibung)
- Family-Refresh-Trigger fällt unter STOPP-Trigger 5 (E81), wenn Modell-Stamm oder Lieferant unklar

**Validiert:** Noch nicht produktiv erprobt — wird beim nächsten Schwester-Artikel-Anlage-Lauf getestet (siehe BACKLOG B52: Schwester-Artikel-Liste).

**Re-Import-Verhalten unverifiziert (B49):** Ob WaWi Cross-Selling-Beziehungen bei Re-Import additiv hinzufügt oder überschreibt, ist noch nicht final geklärt. Bis Verifikation: vor Family-Refresh in WaWi manuell alle existierenden Cross-Selling-Zuweisungen des Modell-Stamms löschen, dann frischen Import.

---

