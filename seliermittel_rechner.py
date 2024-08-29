import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        ertrag_pro_hektar = float(entry_ertrag.get())
        hektarzahl = float(entry_hektar.get())
        
        gesamtertrag = ertrag_pro_hektar * hektarzahl
        packs_needed = gesamtertrag / 100
        
        label_gesamtertrag.config(text=f"Gesamtertrag in to: {gesamtertrag:.2f}")
        label_packs.config(text=f"Benötigte Packungen Siliermittel: {packs_needed:.0f}")
    except ValueError:
        messagebox.showerror("Eingabefehler", "Bitte geben Sie gültige Zahlenwerte ein.")

def reset():
    entry_name.delete(0, tk.END)
    entry_vorname.delete(0, tk.END)
    entry_telefon.delete(0, tk.END)
    entry_ertrag.delete(0, tk.END)
    entry_hektar.delete(0, tk.END)
    label_gesamtertrag.config(text="Gesamtertrag in to:")
    label_packs.config(text="Benötigte Packungen Siliermittel:")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Siliermittel Rechner")

# Kundendaten Eingabe
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Vorname:").grid(row=1, column=0, padx=10, pady=5)
entry_vorname = tk.Entry(root)
entry_vorname.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Telefonnummer:").grid(row=2, column=0, padx=10, pady=5)
entry_telefon = tk.Entry(root)
entry_telefon.grid(row=2, column=1, padx=10, pady=5)

# Ertragsdaten Eingabe
tk.Label(root, text="Ertrag in to FM pro Hektar:").grid(row=3, column=0, padx=10, pady=5)
entry_ertrag = tk.Entry(root)
entry_ertrag.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Hektarzahl:").grid(row=4, column=0, padx=10, pady=5)
entry_hektar = tk.Entry(root)
entry_hektar.grid(row=4, column=1, padx=10, pady=5)

# Berechnung und Ergebnisanzeige
btn_calculate = tk.Button(root, text="Berechnen", command=calculate)
btn_calculate.grid(row=5, column=0, padx=10, pady=20)

btn_reset = tk.Button(root, text="Zurücksetzen", command=reset)
btn_reset.grid(row=5, column=1, padx=10, pady=20)

label_gesamtertrag = tk.Label(root, text="Gesamtertrag in to:")
label_gesamtertrag.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

label_packs = tk.Label(root, text="Benötigte Packungen Siliermittel:")
label_packs.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Hauptfenster starten
root.mainloop()