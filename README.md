# Mini-Taschenrechner

Ein einfacher grafischer Taschenrechner mit Python und Tkinter.

## Funktionen

- ✅ Addition (+)
- ✅ Subtraktion (-)
- ✅ Multiplikation (×)
- ✅ Division (÷)
- ✅ Fehlerbehandlung (ungültige Eingaben, Division durch Null)

## Installation

### Voraussetzungen
- Python 3.11 oder höher
- Tkinter (meist in Python enthalten)

### Setup

1. Repository klonen oder Projekt öffnen
2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Projekt installieren:
   ```bash
   pip install -e .
   ```

## Verwendung

Die Anwendung starten:
```bash
mini-taschenrechner
```

Oder direkt das Skript ausführen:
```bash
python -m mini_taschenrechner
```

### Anleitung
1. Geben Sie die erste Zahl in das linke Eingabefeld ein
2. Geben Sie die zweite Zahl in das rechte Eingabefeld ein
3. Klicken Sie auf eine der Schaltflächen (+, -, ×, ÷)
4. Das Ergebnis wird angezeigt

## Projektstruktur

```
mini-taschenrechner/
├── src/
│   └── mini_taschenrechner/
│       ├── __init__.py
│       └── app.py          # Hauptanwendung
├── pyproject.toml          # Projektkonfiguration
└── README.md              # Diese Datei
```

## Entwicklung

### Tests ausführen
```bash
pytest
```

### Code-Style prüfen
```bash
ruff check .
```

## Lizenz

Dieses Projekt ist Teil eines Schulungsprojekts.
