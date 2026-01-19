# ===================================================================
# Mini-Rechner Anwendung mit Tkinter
# ===================================================================
# Diese Anwendung erstellt einen einfachen grafischen Taschenrechner,
# der die vier Grundrechenarten (Addition, Subtraktion, Multiplikation
# und Division) unterstützt.
# ===================================================================

# Import des tkinter-Moduls für die grafische Benutzeroberfläche (GUI)
import tkinter as tk
from tkinter import font


def calculate(op):
    """
    Führt eine mathematische Berechnung basierend auf dem übergebenen Operator aus.
    
    Diese Funktion liest die Werte aus den beiden Eingabefeldern,
    konvertiert sie in Fließkommazahlen und führt die entsprechende
    Rechenoperation aus.
    
    Parameter:
    ----------
    op : str
        Der mathematische Operator ('+', '-', '*' oder '/')
    
    Fehlerbehandlung:
    -----------------
    - ValueError: Wird ausgelöst, wenn die Eingabe keine gültige Zahl ist
    - Division durch Null: Wird gesondert behandelt und gibt eine Fehlermeldung aus
    """
    try:
        # Einlesen und Konvertieren der ersten Zahl aus dem Eingabefeld entry_a
        a = float(entry_a.get())
        
        # Einlesen und Konvertieren der zweiten Zahl aus dem Eingabefeld entry_b
        b = float(entry_b.get())
        
        # Überprüfung des Operators und Durchführung der entsprechenden Berechnung
        if op == '+':
            # Addition: a + b
            result.set(f"{a + b:.2f}")
        elif op == '-':
            # Subtraktion: a - b
            result.set(f"{a - b:.2f}")
        elif op == '*':
            # Multiplikation: a * b
            result.set(f"{a * b:.2f}")
        elif op == '/':
            # Division: a / b
            if b == 0:
                result.set("Fehler: Division durch 0")
                return
            result.set(f"{a / b:.2f}")
    except ValueError:
        # Fehlerbehandlung für ungültige Eingaben (z.B. Text statt Zahlen)
        result.set("Ungültige Eingabe")


# ===================================================================
# Hauptfenster erstellen und konfigurieren
# ===================================================================

# Erstellen des Hauptfensters (Root-Widget) der Tkinter-Anwendung
root = tk.Tk()

# Setzen des Fenstertitels, der in der Titelleiste angezeigt wird
root.title("Mini-Rechner")
root.geometry("600x250")
root.resizable(False, False)

# Fonts vorbereiten
font_button = font.Font(family="Arial", size=14, weight="bold")
font_input = font.Font(family="Arial", size=12)
font_result = font.Font(family="Arial", size=16, weight="bold")

# ===================================================================
# Eingabefelder erstellen
# ===================================================================

# Erstellen des ersten Eingabefeldes für die erste Zahl
entry_a = tk.Entry(root, font=font_input, width=15, justify="center")

# Erstellen des zweiten Eingabefeldes für die zweite Zahl
entry_b = tk.Entry(root, font=font_input, width=15, justify="center")

# Positionierung des ersten Eingabefeldes im Grid-Layout
entry_a.grid(row=0, column=0, padx=10, pady=10)

# Positionierung des zweiten Eingabefeldes im Grid-Layout
entry_b.grid(row=0, column=1, padx=10, pady=10)

# ===================================================================
# Ergebnis-Label erstellen
# ===================================================================

# Erstellen einer StringVar-Variable zur dynamischen Anzeige des Ergebnisses
result = tk.StringVar()

# Erstellen eines Labels zur Anzeige des Berechnungsergebnisses
tk.Label(root, textvariable=result, font=font_result, bg="#f0f0f0", relief="sunken", height=2).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# ===================================================================
# Operator-Buttons erstellen
# ===================================================================

# Farben für die Buttons (alle gleiche Farbe)
colors = ["#4CAF50", "#4CAF50", "#4CAF50", "#4CAF50"]

# Schleife zur Erstellung der vier Operator-Buttons
for i, (op, color) in enumerate(zip(['+', '-', '*', '/'], colors)):
    tk.Button(root, text=op, font=font_button, width=8, height=2, bg=color, fg="white", command=lambda o=op: calculate(o)).grid(row=2, column=i, padx=10, pady=10)

# ===================================================================
# Clear-Button erstellen
# ===================================================================

def clear():
    """Setzt alle Felder zurück."""
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result.set("")

tk.Button(root, text="Clear", font=font_button, bg="#4CAF50", fg="white", command=clear).grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# ===================================================================
# Hauptprogrammschleife starten
# ===================================================================

# Startet die Tkinter Event-Loop (Hauptschleife)
# Diese Schleife wartet auf Benutzerinteraktionen (Klicks, Tastatureingaben etc.)
# und hält das Fenster geöffnet, bis es vom Benutzer geschlossen wird
root.mainloop()