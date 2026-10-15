# Jukebox – Winterveranstaltung GV 1871 Altenheim

Beamer-Präsentation für die Winterveranstaltung des Gesangverein 1871 Altenheim e.V. (Januar 2027), Motto „Jukebox“. Vor jedem Lied legt eine animierte Jukebox die passende Platte auf und zeigt Titel und Chor bzw. Solist an. Dazu gibt es Übergangsseiten (Pause, Danke) und eine inszenierte Publikumsabstimmung, deren Ergebnis vorher festgelegt ist.

**Live ansehen:** https://pepate.github.io/jukebox/

| Version | Link | Hinweis |
|---|---|---|
| 3D | [Jukebox3D.html](https://pepate.github.io/jukebox/Jukebox3D.html) | three.js, mit Kamerafahrten, braucht etwas Grafikleistung |
| 2D | [Jukebox.html](https://pepate.github.io/jukebox/Jukebox.html) | SVG, läuft auch auf schwachen Rechnern |

Beide Dateien laufen ohne Internet: Schriften, Logo und three.js sind eingebettet.

## Bedienung

| Aktion | Laptop / Presenter | Handy |
|---|---|---|
| Weiter | → / Leertaste / Bild ↓ / Klick | Tippen oder nach links wischen |
| Zurück | ← / Bild ↑ | linker Bildrand oder nach rechts wischen |
| Vollbild | F | erster Tipp (Android) |
| Ton an/aus | M | – |
| Hilfe | H | – |
| Neu starten | Pos1 | Seite neu laden |

Bei der Abstimmung braucht es drei Klicks: Abstimmung starten, Ergebnis abwarten, Gewinner abspielen.

## Programm anpassen

Lieder, Pausen und das Abstimmungsergebnis stehen ganz oben in der jeweiligen HTML-Datei im Block `PROGRAMM`:

```js
{ typ: 'lied', titel: 'Über den Wolken', chor: 'Gemischter Chor' },
{ typ: 'lied', titel: 'Moon River', solist: 'Anna Beispiel' },
{ typ: 'text', titel: 'Pause', text: 'Gleich geht’s weiter …' },
{ typ: 'abstimmung', titel: 'Publikums-Voting', frage: '…', dauer: 12, stimmen: 214,
  ergebnis: [ { titel: 'Über den Wolken', prozent: 19 }, … ] },
```

`TEMPO` regelt, wie schnell die Mechanik arbeitet (1 = gemütlich, 2 = flott).

## Aufbau

```
index.html          Startseite (Auswahl 2D / 3D)
Jukebox.html        2D-Version (gebaut)
Jukebox3D.html      3D-Version (gebaut)
quelle/
  jukebox.src.html    Quelle 2D
  jukebox3d.src.html  Quelle 3D
  build.py            baut Jukebox.html
  build3d.py          baut Jukebox3D.html
  assets/             Schriften, Logo, three.js r160
```

Wenn du nur das Programm änderst, kannst du direkt die fertige HTML-Datei bearbeiten. Änderungen am Design macht man in `quelle/` und baut dann neu:

```bash
python quelle/build.py
python quelle/build3d.py
```

Inhalte im Entwurf (Lieder, Chöre, Abstimmungsergebnis) sind Beispieldaten.
