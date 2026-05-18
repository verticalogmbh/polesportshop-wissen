# ENTSCHEIDUNGS-LOG-STIL-CONTENT-A

**Cluster:** Sprachen, Pricing, Naming, Ameise-Mapping (Teil A)

**Stand:** v1.17, 2026-05-17

**Bezug:** Dieser Cluster ist Teil des Splits der ursprünglichen `ENTSCHEIDUNGS-LOG.md` (v1.16, 165 KB → 6 Themen-Cluster ≤ 40 KB). Historische / abgelöste Einträge liegen weiterhin in `ENTSCHEIDUNGS-LOG-ARCHIV.md`. Cross-Cluster-Referenzen über E-Nummer; der Master-Index mit allen E-Nummern → Cluster-File-Zuordnung liegt in `SPEC_KONSTANTEN.md` unter `ENTSCHEIDUNGSLOG_E_NUMMER_INDEX`.

---

## Index

- **E16** — Standard-Fallbacks für Pflegehinweise und Passform-Defaults
- **E18** — Iterativer Quality-Loop in der Pilot-Phase
- **E22** — HTML- und Stilprofil-Definition für Pipeline-Output
- **E23** — Pricing-Architektur mit zwei Referenztabellen
- **E25** — Pricing-Vereinfachung für Pilot-Phase: Kleidung-only mit Konstante 2.0
- **E26** — Artikelname-Konvention mit Übersetzungstabellen
- **E27** — HotCakes-Größen-Konvention: Kombi-Größen auf kleinste reduzieren
- **E28** — GLD manuell setzbar via Stammdaten-CSV (manuelles Mapping)
- **E29** — Importvorlagen-Naming-Konvention: `{Lieferantenname}_{Nr}_{Import-Typ}`
- **E30** — Spalten-Mapping: sprechende Namen OK, einmaliges manuelles Mapping reicht
- **E31** — Mehrsprachigkeit via "Weitere Texte"-Reiter mit `Global-{Sprache}:`-Präfix
- **E34** — JTL-Erbung-Verbot universalisiert: gilt für Merkmale, Attribute und Bilder
- **E37** — Verkaufskanal-Häkchen müssen aus der Ameise-Importvorlage entfernt werden
- **E38** — GLD-Spalte muss manuell im Ameise-Mapping zugeordnet werden, Auto-Mapping greift nicht
- **E39** — Attribute als Standard-CSV (nicht mehr optional)
- **E55** — SEO-Templates pro Sprache deterministisch aus festem Pattern
- **E56** — Kind-Artikelname mit Größen-Suffix in allen 5 Sprachen; SEO-Felder leben nur auf Vater
- **E58** — Sprach-Lokalisierungs-Konvention für Artikelnamen aus polesportshop-Bestand abgeleitet
- **E59** — WaWi-Mapping-Wissen als „Fels nicht Treibsand" — Schutz-Mechanik gegen Cowork-Erfindungen
- **E72** — Brand-Story-Caching pro Lieferant im `lieferanten_mapping.yaml`
- **E73** — Artikeldetails immer alle 5 Sprachen voll, keine „leichten Übersetzungen mit Eigennamen unverändert"

---

**E16 — Standard-Fallbacks für Pflegehinweise und Passform-Defaults.**
*Warum:* Lieferanten liefern oft nur Sortiments-Daten ohne Detail-Felder. Lauf-Abbruch bei jedem fehlenden Feld wäre zu strikt.
*Verworfen:* Hard-Validierung jedes Feldes (würde >50% der Läufe blockieren).

**E18 — Iterativer Quality-Loop in der Pilot-Phase.**
*Warum:* Edge-Cases sind nicht vorab spezifizierbar. Live-Daten zeigen Lücken, die kein Specification-Workshop findet.
*Verworfen:* Vollständige Pre-Spec aller Lieferanten-Eigenheiten (zu viel Vorab-Aufwand ohne Realitäts-Check).

**E22 — HTML- und Stilprofil-Definition für Pipeline-Output.**
*Warum:* Pipeline produziert Attribut-Inhalte nach festen HTML-Templates pro Attributname statt Quell-HTML aus Crawl-Quellen 1:1 zu übernehmen — sonst entsteht im Shop ein Markup- und Stil-Mischmasch je nach Lieferanten-Herkunft. Plus: konsistentes Du-Form-Stilprofil mit definierter Tonalität, Sprachregister und Werte-Anker.

*Architektur-Entscheidungen (operative Details in cowork_anweisung_datenimports.md Abschnitt 5.4):*
- HTML nach festen Templates pro Attribut (`markentext`, `artikeldetails`, `anwendung`, `faqs`, `material_and_care`, `inhaltsstoffe`, `size_and_fit`)
- Stilprofil mit Du-Form, warm-funktional, ohne Hard-Sell und ohne eingedeutschte Anglizismen
- Custom-CSS-Klassen auf `check` und `h5 bold` beschränkt
- HTML-Entities für deutsche Umlaute (Bestands-Konvention der WaWi)

*Schärfungen 2026-05-14 (nach HotCakes-Lauf):*
- **H1 wird NIE verwendet** — H1 ist im Shop-Template für den Artikelnamen reserviert (Website-SEO). Pipeline-HTML nutzt H2 oder tiefer.
- **Em-Dashes (—) komplett vermeiden** — wirken als KI-Marker. Im Fließtext durch `,` ersetzen, in Taglines durch `:`.
- **Größentabelle aus `size_and_fit` raus** — Tabelle ist zentral im Shop-Template, nicht pro Artikel im Attribut wiederholen.

*Validierung:* JTL-Export *Artikelattribute* vom 13.05.2026 (1742 Zeilen, 537 Artikel, 9 Attribute).

*Vorbehalt:* Stilprofil ist 80-20-Annäherung. Finales CI wird in einer separaten Runde geschärft. Löst die offene Frage in B9.

*Verworfen:* Quell-HTML von Hersteller-Sites 1:1 übernehmen. H1 in Pipeline-Templates (kollidiert mit Website-SEO). Em-Dashes als Stil-Element (KI-Markersignal).

**E23 — Pricing-Architektur mit zwei Referenztabellen.**
*Warum:* Verkaufspreise entstehen beim Artikel-Launch automatisch. Einkäufer-Eingabe pro Lauf bleibt minimal (keine Zoll- und Versandkosten-Frage), und die Faustregel "100% Aufschlag" gilt nicht für alle Warengruppen — Hardware/Hochpreis braucht andere Faktoren.

*Formel:*
```
GLD_netto = EK_netto_Rechnung
          + Zoll_avg_pro_Stück[Lieferant]
          + Versand_avg_pro_Stück[Lieferant]

VK_brutto = GLD_netto × Aufschlagsfaktor[Warengruppe]
          → gerundet auf X,90 (im Zweifel +1 € statt -1 €,
            psychologische Schwellen bei Vollzehnern unterbieten)
```

*Zwei Referenztabellen unter `_PIPELINE/_Referenz/`:*
- `lieferanten_zoll_versand.csv` — Durchschnitt Zoll- und Versandkosten pro Lieferant, gefüttert aus Buchhaltung. Revolvierender Update-Prozess (Details siehe B17).
- `warengruppen_aufschlag.csv` — Aufschlagsfaktor pro Warengruppe. 100% für Apparel als Default, Hardware/Hochpreis abweichend. Manuell gepflegt (Details siehe B18).

*Verworfen:*
- Einheits-Margenfaktor über alle Warengruppen (führt bei Hardware zu unmarktfähigen Preisen).
- Einkäufer-Eingabe pro Lauf für Zoll und Versand (Reibung; fehleranfällig; veraltete Werte zwischen den Läufen).

*Folgeaufgaben:* B17 (Buchhaltungs-Connector), B18 (Initialbefüllung Referenztabellen).
*Implementierung:* cowork_anweisung_datenimports.md v1.2/v1.3.

**E25 — Pricing-Vereinfachung für Pilot-Phase: Kleidung-only mit Konstante 2.0.**
*Stand:* 2026-05-14. Bezug: E23.
*Warum:* E23 sieht zwei Referenztabellen vor (Zoll/Versand pro Lieferant + Aufschlag pro Warengruppe). Für den Pilot reicht ein vereinfachtes Modell: nur Kleidung, fester Aufschlagsfaktor 2.0, eine Referenztabelle. Technik kommt später (Charter-Prinzip 9).
*Formel (Pilot):*
```
GLD_netto = EK_Rechnung + Zoll_pro_Stück + Versand_pro_Stück
VK_brutto = GLD_netto × 2.0 → gerundet auf X,90
            mit Vollzehner-Unterbietung (39,90 € statt 40,90 € bei roh 40,xx)
```
*Eine Referenztabelle:* `lieferanten_zoll_versand.csv` (statt zwei). Aufschlagsfaktor 2.0 ist Konstante, nicht aus Tabelle.
*Hot Cakes-Anwendung:* Hekate Bodysuit EK 39,00 € → GLD 39,00 (Zoll 0, Versand 0) → VK roh 78,00 → VK gerundet 77,90 €.
*Verworfen für Pilot:* Warengruppen-Tabelle mit Cluster Kleidung+Technik (verschoben in B-Backlog, Reaktivierung wenn Technik-Pipeline startet).

**E26 — Artikelname-Konvention mit Übersetzungstabellen.**
*Stand:* 2026-05-14.
*Warum:* Artikelnamen sind kanonisch, klar formelhaft, multilingual ableitbar. Format soll konsistent über alle Lieferanten und Sprachen funktionieren.
*Format:* `{Hersteller} {Kleidungstyp} {Modell} {Farbe}`
*Beispiel HotCakes:*
- DE: `HotCakes Bodysuit Hekate Schwarz`
- EN: `HotCakes Bodysuit Hekate Black`
- ES: `HotCakes Body Hekate Negro`
- IT: `HotCakes Body Hekate Nero`
- FR: `HotCakes Body Hekate Noir`
*Übersetzungs-Tabellen (Auszug):*
- Kleidungstyp: Top/Top/Haut, Shorts/Shorts/Short/Pantalones Cortos, Bodysuit/Body, Sticky/Appiccicoso
- Farbe: Schwarz/Black/Negro/Nero/Noir, …
*Print-Designs:* Artikelname bleibt simpel ohne Print-Bezeichnung. Print-Details kommen in das Attribut `artikeldetails` (Teil von E22).
*Verworfen:* Print-Bezeichnung im Artikelnamen (würde Konvention sprengen, schlechtere Sortierbarkeit).

**E27 — HotCakes-Größen-Konvention: Kombi-Größen auf kleinste reduzieren.**
*Stand:* 2026-05-14. Bezug: E8 (Override für HotCakes).
*Warum:* HotCakes liefert Kombi-Größen-SKUs wie `XS/S`. E8 würde dafür zwei Filter-Werte (XS und S) auf dem Kind ablegen, damit Filter-Suche nach S das Produkt findet. Tjorben hat sich beim HotCakes-Stage-Run gegen diese Expansion entschieden: SKU bleibt `XS`, Filter-Wert auch `XS`. Begründung: bei HotCakes ist die Größe `XS/S` faktisch ein XS-Schnitt mit minimaler Toleranz nach oben. Kunden, die nach S filtern, sind nicht die Zielgruppe für `XS/S`.
*Implementierung:* Lieferanten-spezifisches Feld `groessen_konvention` im `lieferanten_mapping.yaml`. Werte: `standard` (jede Größe einzeln, E8-Default) oder `kombi_reduziert_auf_kleinste` (HotCakes).
*Verworfen:* E8 universell anwenden (passt nicht zur HotCakes-Realität). Größen-Logik global hardcoden (verträgt nicht mehrere Lieferanten-Eigenheiten).

**E28 — GLD manuell setzbar via Stammdaten-CSV (manuelles Mapping).**
*Stand:* 2026-05-14. Bezug: E23, E38.
*Warum:* JTL berechnet den GLD ("Gleitender Durchschnittspreis", Feld "Ø Einkaufspreis (netto)") aus Eingangsrechnungen automatisch. Im Pilot wollen wir den GLD manuell pro Stück nach E23-Formel setzen, ohne Eingangsrechnungs-Verbuchung (Buchhaltungs-Aufwand). Validierung beim HotCakes-Stammdaten-Lauf 2026-05-14: Spalte `EK Netto (für GLD)` in der Stammdaten-CSV greift, **wenn beim Mapping manuell zugeordnet** (Auto-Mapping greift nicht zuverlässig). Vorlage speichert das danach dauerhaft (siehe E38).
*Verworfen:* Separater QuickSync-Import. Lagerbestand-Trick. Eingangsrechnungs-Workflow.

**E29 — Importvorlagen-Naming-Konvention: `{Lieferantenname}_{Nr}_{Import-Typ}`.**
*Stand:* 2026-05-15 (E46-konform, 4 Vorlagen pro Lieferant).
*Warum:* JTL-Ameise zwingt pro Lieferant eine eigene Vorlage (Lieferant ist Pflichtfeld beim Speichern). Bei 50 Lieferanten × 4 Vorlagen = 200 Vorlagen total. Pro Import-Typ filtert Ameise eh, also pro Schritt nur 50 sichtbar — Lieferantenname zuerst bringt natürliche Sortierung im Vorlagen-Dropdown.

*Naming:* `{Lieferantenname}_{Reihenfolge}_{Import-Typ}` mit Underscores als Element-Trenner. Leerzeichen nur innerhalb des Lieferantennamens. Beispiel: `HotCakes Polewear_1_Stammdaten`.

*Reihenfolge (4 Vorlagen seit E46):*
1. `{Lieferantenname}_1_Stammdaten` (inkl. Bild-Spalten und Bilder/Plattformen-Konfiguration)
2. `{Lieferantenname}_2_Variationen`
3. `{Lieferantenname}_3_Merkmale`
4. `{Lieferantenname}_4_Attribute`

*Bestands-Lieferanten:*
- *HotCakes:* historisches Naming `_1_Stammdaten`, `_2_Variationen`, `_3_Lieferantendaten` (legacy via E35), `_4_Merkmale`, `_5_Bilder` (legacy via E46). Stammdaten-Vorlage 2026-05-15 um Bild-Mapping (Bild 1-4 erstmal, Ausbau auf 1-10 anstehend) plus „Bilder/Plattformen"-Häkchen für alle 11 Plattformen erweitert. Eine `_4_Attribute`-Vorlage muss neben den Bestand ergänzt werden (im 2026-05-14er Pilot ad-hoc importiert).
- *POLE ADDICT:* folgt noch altem Naming (`POLE ADDICT Stammdaten Import`). Nicht umbenennen — Vorlagen funktionieren. Nur neue Lieferanten folgen E29.

*Verworfen:* Import-Typ zuerst (Ameise filtert eh nach Import-Typ). Mittelpunkt `·` als Trenner (Underscore tipp-freundlicher).

**E30 — Spalten-Mapping: sprechende Namen OK, einmaliges manuelles Mapping reicht.**
*Stand:* 2026-05-14.
*Warum:* JTL-Ameise auto-matched Spaltennamen nur teilweise. Im HotCakes-Test griff Auto-Mapping bei `Brutto-VK` (JTL-Feldname), nicht aber bei `EK Netto (für GLD)`. Konsequenz: Spaltennamen zwanghaft auf JTL-Feldnamen zu trimmen bringt nur eingeschränkten Nutzen — pro Lieferant wird ohnehin **einmal** manuell gemappt + Vorlage gespeichert, danach pro neuem Lieferanten geklont. Sprechende Spaltennamen sind dadurch OK.
*Konsequenz für die Pipeline:* CSV-Spaltennamen dürfen klar und beschreibend sein, müssen nicht 1:1 JTL-Feldnamen treffen. Auto-Mapping ist ein Bonus, kein Designziel.
*Verworfen:* Alle CSV-Spalten zwanghaft auf JTL-Feldnamen prüfen (Aufwand ohne Mehrwert). Eigene CSV-Naming-Konvention ohne Bezug zu JTL-Feldnamen (würde Mapping-Debugging erschweren, schlechte Lesbarkeit).

**E31 — Mehrsprachigkeit via "Weitere Texte"-Reiter mit `Global-{Sprache}:`-Präfix.**
*Stand:* 2026-05-14.
*Warum:* JTL-Ameise hat im Import-Dialog einen Reiter "Weitere Texte" (unten, neben "Einstellungen") für sprach-spezifische Felder (Artikelname, Titel-Tag, Meta-Description, Variationsname, Variationswertname pro Sprache). Die Felder erscheinen NICHT im normalen Mapping-Bereich, sondern explizit nur in diesem Reiter. CSV-Spalten mit Präfix `Global-Englisch:`, `Global-Französisch:`, `Global-Italienisch:`, `Global-Spanisch:` werden dort den entsprechenden Sprach-Feldern zugewiesen.
*Konvention:* Pipeline produziert für jede mehrsprachige Spalte eine eigene CSV-Spalte mit dem Präfix-Schema `Global-{Sprache}: {Feldname}`. Beispiele: `Global-Englisch: Artikelname`, `Global-Französisch: Titel-Tag`, `Global-Italienisch: Variationswertname`.
*Quelle:* Konvention stammt aus Tjorbens Best-Practice-Vorlage `meta_daten.csv` und wurde im HotCakes-Lauf validiert.
*Verworfen:* Sprach-Spalten ohne Präfix benennen (würde mit deutschen Feldern kollidieren oder Auto-Mapping verwirren). Separate Sprach-Importe (zusätzlicher Schritt pro Sprache, ineffizient).

**E34 — JTL-Erbung-Verbot universalisiert: gilt für Merkmale, Attribute und Bilder.**
*Stand:* 2026-05-14. Erweiterung von E19. *Schärfung 2026-05-15:* gilt unverändert auch nach Integration der Bilder in die Stammdaten-CSV (E46).
*Warum:* E19 hat etabliert, dass Merkmale explizit auf Vater UND Kindern gepflegt werden müssen, weil JTL nichts implizit erbt. Während des HotCakes-Pilots hat sich gezeigt: dieselbe Logik gilt für Attribute (HotCakes-Attribute-Import 2026-05-14 ad-hoc auf 16 Zeilen Vater + Kinder ausgeweitet von ursprünglich 12 Zeilen nur Vater) und für Bilder (Tjorbens etablierte Praxis: Bilder werden manuell auf alle Kinder eines Stamms vererbt, weil sonst Inkonsistenzen entstehen).
*Regel:* JTL erbt zwischen Vater und Kind generell nichts implizit. Pipeline-Output muss Merkmale, Attribute und Bilder explizit pro Artikel (Vater UND jedes Kind) pflegen.
*Implementierung:*
- Merkmale: schon in E19, Spec v1.2 etabliert.
- Attribute: cowork_anweisung_datenimports.md v1.3 erweitert; HotCakes-Lauf 2026-05-14 mit 64 Zeilen (16 Artikel × 4 Attribute).
- Bilder: cowork_anweisung_bildpipeline.md v1.1 erweitert; CSV produzierte eine Zeile pro Artikel × Bild (Vater + alle Kinder × N Bilder).
*Schärfung 2026-05-15 nach E46:* Die Erbung-Regel bleibt bestehen — sie wird jetzt durch die Struktur der Stammdaten-CSV abgebildet. Jeder Artikel-Eintrag (Vater UND jedes Kind) bekommt seine eigene Zeile mit identischen Bild-URLs in den Spalten `Bild 1` bis `Bild N`. Die Pipeline-Stage „Bilder auf Kinder duplizieren" entfällt nicht — sie geschieht jetzt durch Spalten-Befüllung in der Stammdaten-Zeile statt durch Zeilen-Duplizierung in einer separaten Bilder-CSV.
*Verworfen:* Implizite Vererbung annehmen, nur Vater pflegen (führt zu leeren Kind-Detailseiten und Filter-Lücken).

**E37 — Verkaufskanal-Häkchen müssen aus der Ameise-Importvorlage entfernt werden.**
*Stand:* 2026-05-14. Bezug: B21.
*Warum:* Beim HotCakes-Stammdaten-Import gingen Artikel sofort online — weil die Ameise-Importvorlage rechts oben im Standardwerte-Bereich "Verkaufskanal aktiv" alle Häkchen (polesportshop.de, poledanceshop.de, Mobile Kasse) defaultmäßig gesetzt hatte. Pipeline-Logik geht aber davon aus, dass Artikel erst nach Review aktiviert werden.
*Konvention:* Bei Anlage einer neuen Lieferanten-Stammdaten-Vorlage werden die Verkaufskanal-Häkchen entfernt und die Vorlage gespeichert. Tjorben aktiviert pro Artikel manuell nach Review (Pilot-Workaround). Mittelfristig: pro Verkaufskanal eine CSV-Spalte mit Default "N" (B21).
*Verworfen:* Häkchen drinlassen und Artikel pro Lauf manuell deaktivieren (umständlich, fehleranfällig). Vorlage nicht speichern (jedes Mal beim Import dran denken — gleicher Fehler).

**E38 — GLD-Spalte muss manuell im Ameise-Mapping zugeordnet werden, Auto-Mapping greift nicht.**
*Stand:* 2026-05-14. Bezug: E28.
*Warum:* HotCakes-Stammdaten-Lauf hat gezeigt: bei der CSV-Spalte `EK Netto (für GLD)` greift Ameise-Auto-Mapping nicht — ohne manuelle Spalten-Zuordnung im Mapping-Dialog bleibt der GLD-Wert beim Artikel leer. Andere Spalten wie `Brutto-VK` greifen Auto-Mapping problemlos.
*Konvention:* Bei der einmaligen Anlage der Stammdaten-Vorlage pro Lieferant wird `EK Netto (für GLD)` manuell auf das JTL-Feld "Ø Einkaufspreis (netto)" gemappt und die Vorlage gespeichert. Danach greift es bei jedem folgenden Lauf.
*Verworfen:* Spalten-Name auf JTL-Default zwingen (würde das Problem nicht lösen — Auto-Mapping greift offenbar generell unzuverlässig bei diesem Feld). QuickSync-Workaround (Forum-Vorschlag, ist im Pilot nicht nötig).

**E39 — Attribute als Standard-CSV (nicht mehr optional).**
*Stand:* 2026-05-14. Bezug: E22.
*Warum:* Pipeline v1.2 hatte Attribute als "optional, sobald Reichtext-Phase aktiv" markiert. HotCakes-Pilot 2026-05-14 hat aber gezeigt: Attribute werden für jeden produktiven Artikel gebraucht (markentext, artikeldetails, material_and_care, size_and_fit), und die HTML-Templates aus E22 sind etabliert. Es gibt keinen Grund mehr, Attribute optional zu halten.
*Konvention ab 2026-05-14:* Attribute-CSV wird bei jedem Pipeline-Lauf erzeugt (Position 4 in der Import-Reihenfolge nach E35). Eine Zeile pro Artikel × Attribut (Vater + alle Kinder gemäß E34). Mindestens die vier Kern-Attribute markentext, artikeldetails, material_and_care, size_and_fit. anwendung, faqs, inhaltsstoffe je nach Produkt-Relevanz.
*Verworfen:* Attribute weiterhin als optional führen (führt zu inkonsistenter Pflege, nicht alle Artikel haben dieselben Datentiefe).

**E55 — SEO-Templates pro Sprache deterministisch aus festem Pattern.**
*Stand:* 2026-05-15 spät. Bezug: E26 (Artikelname), E31 (Mehrsprachigkeit).

*Warum:* Im 3-Modell-Cowork-Batch hat Cowork eigene produkt-spezifische Meta-Descriptions erfunden („Mesh-Bodysuit mit Marmor-Print, tiefem Ausschnitt..."). Tjorben hat im JTL-Export `JTL-Export-Artikelstammdaten-15052026.csv` (802 Datenzeilen, 297 davon mit allen 5 Sprach-Feldern) ein 100 % konsistentes Pattern über 30 Stichproben-Artikel hinweg verifiziert: alle Titel-Tags und Meta-Descriptions folgen einem festen Template pro Sprache, mit dem Artikelnamen als einziger Variable. Cowork-Erfindung ist deshalb anti-pattern — die richtigen Werte stehen seit Jahren so im Shop und sind in Stein gemeißelt.

*Entscheidung — Pattern fest verankert (rein deterministisch, einzige Variable = `{name}`):*

```
Titel-Tag pro Sprache:
   DE:  <name> | polesportshop.de
   EN:  <name> | polesportshop.de   ← EN nutzt auch .de, nicht .com
   FR:  <name> | polesports.fr
   IT:  <name> | polesports.it
   ES:  <name> | polesports.es

Meta-Description pro Sprache (HTML-Entities &#10004; = ✓ und &#10148; = ➜):
   DE:  <name> &#10004; große Auswahl &#10004; TOP Preise &#10004; Schneller Versand &#10148; jetzt hier online bestellen!
   EN:  <name> &#10004; Five star customer support &#10004; Top quality and price &#10004; Instant shipping &#10148; order now!
   FR:  <name> &#10004; Support client cinq étoiles &#10004; Qualité et prix au top &#10004; Expédition instantanée &#10148; commandez maintenant !
   IT:  <name> &#10004; Assistenza clienti a cinque stelle &#10004; Qualità e prezzo al top &#10004; Spedizione immediata &#10148; ordina ora!
   ES:  <name> &#10004; Soporte al cliente de cinco estrellas &#10004; Calidad y precio superiores &#10004; Envío instantáneo &#10148; ¡Ordénalo ahora!
```

*Konsequenzen:*
- SEO-Felder leben **nur auf Vater-Zeile**. Variable `{name}` ist der **Vater-Artikelname ohne Größe**. Kinder haben SEO-Felder leer.
- Cowork hat hier keinen kreativen Spielraum mehr — kein „produkt-spezifischer Spin", keine USP-Variationen, keine kontextuelle Anpassung. Reine String-Substitution.
- Pattern ist HTML-Entity-kodiert (`&#10004;` statt `✓`, `&#10148;` statt `➜`). Unicode-Zeichen direkt einsetzen wäre falsch — Tjorbens Shop erwartet die Entities so wie sie historisch da sind.
- Die produkt-spezifische Beschreibung lebt im Attribut `artikeldetails` mit E53-Stil (polesportshop-DNA + Pole-Junkie-Reduktion), klar getrennt von den SEO-Metadaten.

*Verworfen:*
- *Produkt-spezifische Meta-Descriptions (Cowork-3-Modell-Batch-Stand):* schöne Cowork-Outputs, aber inkompatibel mit dem historischen Shop-Pattern und Quelle echter Re-Import-Probleme. Außerdem nicht reproduzierbar.
- *Pattern-Variation pro Saison/Kampagne:* unnötige Variabilität für Kleidungs-Pilot; späteres Marketing-Tooling kann das übernehmen, falls je nötig.
- *Eigene EN-Domain `polesportshop.com`:* existiert nicht im Bestand. EN-Titel-Tags nutzen `polesportshop.de` (im Export bestätigt).

---

**E56 — Kind-Artikelname mit Größen-Suffix in allen 5 Sprachen; SEO-Felder leben nur auf Vater.**
*Stand:* 2026-05-15 spät. Bezug: E26, E55.

*Warum:* Beim ersten v3.1-Stammdaten-Re-Import 2026-05-15 spätabends zeigte WaWi alle Kind-Artikel mit identischem Namen zum Vater (z.B. „HotCakes Bodysuit Hekate Schwarz" für alle vier Größen XS-L). Pattern-Check im JTL-Export: 453 Artikel haben Größe am Namens-Ende, 349 ohne (Väter mit Variation + One-Size-Artikel). Konvention im Shop ist klar: Kind = Vater-Name + Leerzeichen + Variationswert.

*Entscheidung:*
- **Vater-Artikelname (alle 5 Sprachen):** ohne Größe — z.B. `HotCakes Bodysuit Hekate Schwarz`, `HotCakes Body Hekate Noir` (FR)
- **Kind-Artikelname (alle 5 Sprachen):** Vater-Name + Leerzeichen + Variationswert — z.B. `HotCakes Bodysuit Hekate Schwarz XS`, `HotCakes Body Hekate Noir XS`
- **SEO-Felder (Titel-Tag, Meta-Description in allen 5 Sprachen):** leben **ausschließlich auf der Vater-Zeile** und nutzen den Vater-Namen ohne Größe. Auf Kind-Zeilen sind alle 10 SEO-Spalten leer.

*Konsequenzen:*
- Cowork muss bei Kind-Generierung sowohl den DE-Namen als auch alle 4 Sprach-Namen mit Größe-Suffix ergänzen, nicht nur den DE-Namen.
- Bei Multi-Kategorie-Doppelzeilen (E57) gilt das pro Doppelzeile — SEO auf den beiden Vater-Zeilen, leer auf den beiden Kind-Zeilen pro Größe.

*Verworfen:*
- *Kind erbt Namen unverändert vom Vater:* macht WaWi-UI unbrauchbar (alle vier Größen heißen gleich, keine Unterscheidung in Listen).
- *Größe via Bindestrich (`Hekate Schwarz-XS`) oder Slash (`Hekate Schwarz/XS`):* widerspricht dem etablierten Shop-Pattern (Leerzeichen + Größe, validiert in 453 Bestand-Artikeln).
- *Größe nur im DE-Namen, Sprach-Namen ohne Größe:* führt zu Inkonsistenz im Shop bei Sprachwechsel; aus dem Export ist klar dass alle 5 Sprachen die Größe konsistent am Ende führen.

---

**E58 — Sprach-Lokalisierungs-Konvention für Artikelnamen aus polesportshop-Bestand abgeleitet.**
*Stand:* 2026-05-15 spät. Bezug: E26.

*Warum:* Aus dem JTL-Export 2026-05-15 (802 Artikel, 297 mit allen 5 Sprachen gepflegt) lässt sich eine eindeutige Lokalisierungs-Konvention ableiten — sie war bisher nur implizit in E26 verankert, jetzt explizit fest verankert. Cowork hat in vorherigen Läufen Sprach-Namen teils erfunden (z.B. „Türkis" als „Blue" statt „Teal").

*Konvention (aus Bestand abgeleitet, 30 Stichproben über mehrere Brands):*

| Element | Behandlung | Beispiele |
|---|---|---|
| **Brand-Name** | unverändert in allen 5 Sprachen | HotCakes, FANNA, Polerina, Pole Addict, Shark Polewear, Dragonfly, Lunalae, Paradise Chick, Bandurska |
| **Eigennamen (Modell-Namen)** | unverändert in allen 5 Sprachen | Hekate, Arachne, Savanna, Emma, Carla, Monica, Isla, „Bali Grape", „X Spark Edition" |
| **Produkt-Substantiv** | meist lokalisiert (s. Tabelle unten) | „Bodysuit" → „Body" (FR/IT/ES); „Shorts" → „Short" (FR), „Pantalones Cortos" (ES); „Top" → „Haut" (FR) |
| **Material/Style-Substantiv** | meist lokalisiert | „Mesh" → „Maille" (FR), „Maglia" (IT), „Malla" (ES); „Velvet" bleibt überall |
| **Farb-Adjektiv** | konsequent lokalisiert | Schwarz/Black/Noir/Nero/Negro; Türkis/Teal/Turquoise/Turchese/Turquesa; Burgundrot/Burgundy/Borgogna/Burdeos |
| **Größen-Suffix** | identisch in allen Sprachen | XS, S, M, L, XL, 2XL (universal) |

**Produkt-Substantiv-Übersetzungstabelle (explizit, weil häufig falsch):**

| DE | EN | FR | IT | ES |
|---|---|---|---|---|
| Bodysuit | Bodysuit | Body | Body | Body |
| Shorts | Shorts | Short | Shorts | Pantalones Cortos |
| Top | Top | Haut | Top | Top |
| Leggings | Leggings | Legging | Leggings | Leggings |

**Farb-Übersetzungstabelle (häufig in Pole-Wear, explizit):**

| DE | EN | FR | IT | ES |
|---|---|---|---|---|
| Schwarz | Black | Noir | Nero | Negro |
| Weiß | White | Blanc | Bianco | Blanco |
| Türkis | Teal | Turquoise | Turchese | Turquesa |
| Pink | Pink | Rose | Rosa | Rosa |
| Burgundrot | Burgundy | Bordeaux | Borgogna | Burdeos |
| Beige | Beige | Beige | Beige | Beige |

*Konsequenzen:*
- Cowork hat eine geschlossene Übersetzungs-Lookup-Tabelle für die typischen Pole-Wear-Begriffe — keine LLM-Übersetzung nötig für Standard-Vokabular.
- Bei seltenen oder neuen Begriffen (z.B. exotischer Farb-Name) darf Cowork übersetzen, muss das aber im Lauf-Bericht markieren.
- Bei Eigennamen (Modell-Namen wie „Hekate") gilt: nie übersetzen.

*Verworfen:*
- *Vollständige LLM-Übersetzung pro Sprache pro Begriff:* überdimensioniert + reproduzierbare Fehler bei Pole-Wear-Vokabular.
- *Eigene Pflegetabelle pro Lieferant:* unnötig, weil Pole-Wear-Begriffe lieferanten-übergreifend stabil sind.

---

**E59 — WaWi-Mapping-Wissen als „Fels nicht Treibsand" — Schutz-Mechanik gegen Cowork-Erfindungen.**
*Stand:* 2026-05-15 spät. Bezug: alle E50-E58, generell.

*Warum:* Über zwei Stammdaten-Import-Sessions (3-Modell-Cowork-Batch und v3.1-Pre-22-Test 2026-05-15) hat Cowork mehrfach Wissen erfunden statt aus den Wissens-Files abgerufen. Konkrete Vorfälle:

1. **Kategorie „Damen" erfunden** statt aus E51-Mapping abrufen (resultierende WaWi-Anzeige falsch)
2. **Artikelname „Blau" geschrieben** statt aus E50-Farb-Logik die zweistufige Konvention abrufen („Türkis" spezifisch + WaWi-Wert „Blau" im Merkmal)
3. **Meta-Descriptions selbst getextet** (produkt-spezifische Sätze) statt aus dem fest etablierten Shop-Pattern (E55)
4. **Spalten-Reihenfolge umorganisiert** (Lieferantenblock auf Position 16-17) statt aus E54 die ALT-Reihenfolge der Vorlage respektieren
5. **Kind-Artikelname ohne Größe** statt aus E26+E56 die Größen-Suffix-Konvention abrufen
6. **Multi-Kategorie unbekannt** statt E57-Recherche im Forum durchführen (Forum-Pattern war 12+ Jahre alt verfügbar)

Tjorbens Sicht (zentral): „Insbesondere das WaWi-Wissen, das muss echt in Stein gemeißelt werden, weil da ist ganz wenig Änderung. Da hatte ich jetzt das Gefühl, das ist wie Treibsand."

*Diagnose:* Die einzelnen Wissens-Files (`WAWI-IMPORT-WISSEN.md`, `cowork_anweisung_datenimports.md`) waren strukturell verteilt, aber nicht als **kanonisch-unverhandelbar** markiert. Cowork hat keine prozedurale Pflicht zur Konsultation vor CSV-Generation gehabt — Wissens-Abruf war optional statt verpflichtend. Konsequenz: Cowork füllt Lücken mit LLM-Generation, die zwar plausibel klingt, aber nicht dem Shop-Bestand entspricht.

*Entscheidung — vier Schutz-Mechaniken:*

1. **Charter-Prinzip 12 (neu):** „WaWi-Mapping ist gefrorenes Wissen — niemals erfinden, immer konsultieren". Macht das Prinzip zu einer harten Architektur-Regel, nicht nur einem Detail.

2. **Header-Markierung in `WAWI-IMPORT-WISSEN.md`:** Klare „🔒 KANONISCH" Markierung am Datei-Anfang. Erklärt explizit: jedes Detail in dieser Datei ist aus echten WaWi-Import-Läufen empirisch validiert. Trial-and-Error-Kosten dieser Erkenntnisse sind bekannt (Stunden bis Tage). Niemals durch generierte Plausibilität ersetzen.

3. **Konsultations-vor-Aktion-Workflow in `cowork_anweisung_datenimports.md`:** Stage 6 (Validierung) erweitert um eine **Mapping-Bibel-Self-Check-Checkliste** mit 12 expliziten Prüf-Punkten. Cowork muss diese Checkliste vor Stage 7 (CSV-Schreiben) durchgehen und im Lauf-Bericht dokumentieren. Anti-Pattern-Liste mit den konkreten 6 Cowork-Erfindungen aus dieser Session als „so nicht"-Beispiele.

4. **Referenz-Artikel-Konvention:** Die drei HotCakes-Artikel Hekate Bodysuit, Arachne Bottom Teal, Savanna Original Top sind ab v1.9 als **„Goldstandard"** deklariert. Cowork muss jeden neuen Artikel strukturell gegen diese drei vergleichen — wenn ein Feld bei einem neuen Artikel anders aussieht als bei den Goldstandard-Artikeln (ohne dass ein Lieferanten-Mapping-Eintrag dafür existiert), STOPP + User-Frage.

*Konsequenzen:*
- Klar abgegrenzte „Stein-gemeißelte" vs. „in Bewegung" Wissens-Bereiche. WaWi-Mapping = Stein; Lieferanten-Mapping und Pricing-Tabellen = in Bewegung; Stil-Briefing = teilweise in Bewegung (E53).
- Cowork-Lauf-Bericht enthält ab v1.9 einen expliziten „Mapping-Bibel-Self-Check"-Abschnitt mit pro-Punkt-Bestätigung.
- Bei Self-Check-Verletzung: Cowork bricht den Lauf ab, statt eine plausible Erfindung in die CSV zu schreiben.
- Goldstandard-Artikel sind im Lauf-Bericht als Referenz hinterlegt.

*Verworfen:*
- *Read-only-Markierung der Wissens-Files:* technisch nicht durchsetzbar, weil Tjorben + Claude selbst noch Updates schreiben.
- *Versions-Diff vor CSV-Generation:* zu komplex für Pilot, würde Cowork-Logik aufblähen.
- *LLM-Cross-Check via zweites Modell:* nicht skalierbar, plus die zweite Instanz hätte den gleichen Bias.
- *Allein auf System-Prompt-Hinweise vertrauen:* das war der bisherige Stand, hat in 2 von 2 Stammdaten-Sessions versagt.

---

**E72 — Brand-Story-Caching pro Lieferant im `lieferanten_mapping.yaml`.**
*Stand:* 2026-05-16. Bezug: Baseline-Lauf Sektion 5.4 (Markentext eigenformuliert, als E70-Eigeninterpretation markiert), E70 (Feature-Erfassung text-basiert).

*Warum:* Im Baseline-Lauf hat Cowork den Markentext für HotCakes Polewear pro Lauf neu generiert („Griechenland, Sport-First, Print-Serien"), als E70-Eigeninterpretation markiert. Das wird sich beim nächsten HotCakes-Lauf wiederholen — leicht anders formuliert, Token-Aufwand pro Lauf, Markenposition nicht stabil über Läufe. Brand-Story ist pro Lieferant stabil, nicht pro Artikel oder Lauf. Logischer Cache-Ort: `lieferanten_mapping.yaml`.

*Entscheidung:*
- Neue optionale Felder pro Lieferant: `brand_story_de`, `brand_story_en`, `brand_story_fr`, `brand_story_it`, `brand_story_es`. Jeweils ~80-150 Wörter, im polesportshop-DNA-Ton (siehe E74-Stil-Pivot).
- Wenn die Felder gepflegt sind: Cowork verwendet sie 1:1 als `markentext`-Attribut, KEIN E70 mehr nötig.
- Wenn die Felder `null` sind: Cowork generiert wie bisher pro Lauf, markiert als E70.
- Erste Version für HotCakes Polewear wird in v1.13 angelegt, basierend auf dem Brand-Material aus dem Baseline-Lauf (Griechenland, Print-Serien, Pole-Dance-Performance-First).
- Pflege-Konvention: bei Tjorben. Bei jedem neuen Lieferanten kuratiert er einmalig die Brand-Story über alle 5 Sprachen — analog zur Pflicht-Pflege von `hersteller` und `marke_kurz`.

*Konsequenzen:*
- Stabilere Markenposition über Läufe.
- Token-Ersparnis pro HotCakes-Lauf (5 Sprachen × ~100 Wörter sind nicht-trivial).
- Tjorben investiert ~20 min pro Lieferant beim Onboarding für die Brand-Story-Pflege.
- Wenn ein Hersteller seine Marken-Botschaft ändert: Mapping-Update statt Lauf-Reset.

*Verworfen:*
- *Brand-Story in eigenes File pro Lieferant auslagern:* würde Files-Zahl im Snapshot aufblähen, der Mapping-Eintrag selbst ist die richtige Granularität.
- *Brand-Story dynamisch aus Shopify-Über-uns-Seite crawlen:* zusätzlicher Crawl-Step, fragile Quelle, ändert sich plötzlich. Manuelle Kuration einmalig ist robuster.

---

**E73 — Artikeldetails immer alle 5 Sprachen voll, keine „leichten Übersetzungen mit Eigennamen unverändert".**
*Stand:* 2026-05-16. Bezug: Baseline-Lauf Sektion 5.3, E70 (Feature-Erfassung), E31 (Mehrsprachigkeit).

*Warum:* Im Baseline-Lauf waren DE-Texte vollwertig in polesportshop-DNA, EN/FR/IT/ES als „leichte Übersetzungen mit Brand-/Modell-/Print-Eigennamen unverändert" markiert — als E70 für sprachliche Feinabstimmung später aufgeschoben. Tjorbens explizite Ansage: alle Sprachen voll, gleicher Qualitätsanspruch wie DE. Kein Halt auf halber Strecke, weil der internationale Shop genauso wichtig ist wie DE.

*Entscheidung:*
- Alle 5 Sprachen (DE, EN, FR, IT, ES) im `artikeldetails`-Attribut werden **voll** ausformuliert. Eigene Stimme pro Sprache, nicht 1:1-Übersetzung aus DE.
- Eigennamen unverändert lassen (Brand, Modell, Print-Familien) — das bleibt aus E58.
- Pro Sprache eigene Tonalität-Treffer entsprechend Lokalisierung (FR sinnlicher, IT lebhafter, ES warm-direkt, EN cool-confident, DE warm-funktional mit Esprit).
- Kein E70 mehr für Sprach-Halbgar-Markierung — Sprachen sind ab v1.13 Pflicht-vollwertig.
- Cowork-Token-Mehrverbrauch wird akzeptiert.

*Konsequenzen:*
- ~20 % Token-Anstieg pro Artikel (geschätzt) gegenüber Baseline.
- Internationale Shop-Qualität entspricht endlich der DE-Qualität.
- Übersetzungs-Konsistenz für Eigennamen muss strikt eingehalten werden — siehe E58 / SPEC_KONSTANTEN Sektion 6.

*Verworfen:*
- *DE als Master, EN/FR/IT/ES als deterministische Übersetzung via Haiku-Translation-Layer:* würde Tokens sparen, ist aber tonal flacher und braucht eine zweite Modell-Spur. Aufgeschoben in B47 falls Token-Kosten relevant werden.
- *Englisch als Lingua Franca für Nicht-DE-Märkte:* würde Conversion verlieren, Polesportshop hat klare Multi-Sprach-Strategie.

---
