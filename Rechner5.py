# Bibliothek importieren
from math import *
from tkinter import *
from tkinter import messagebox
import tkinter


# Ein Fenster bauen
Fenster = Tk()

# ===================================Einstellungen==========================================

# die Länge und Breite des Fensters festsetzen
Fenster.geometry("432x270")
# Fenstergrösse beschränken
Fenster.resizable(width=False, height=False)
# Titel zum Fenster hinzufügen
Fenster.title('Rechner')


# ===================================Funktionen==========================================

Operator = ""

# Funktion zur Anzeige von Fehlern


def errorMsg(ms):
    if ms == 'Error':
        tkinter.messagebox.showerror('Error', 'Irgenwas stimmt nicht')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror(
            'Division Error', 'Kann nicht durch Null geteilt werden')


# Funktion zum klicken auf den Tasten
def btn_klick(Nummern):
    try:
        global Operator
        Operator += str(Nummern)
        derText_desEingangs.set(Operator)
    except:
        errorMsg('Error')


# Funktion zum löschen
def btn_entfernen():
    try:
        global Operator
        Operator = " "
        derText_desEingangs.set(Operator)
    except:
        errorMsg('Error')


# Tastenfunktionen +-*/
def btn_kalkulieren(Symbole):
    try:
        global Operator
        Operator += str(Symbole)
        derText_desEingangs.set(Operator)
    except:
        errorMsg('Error')


# Funktion zur die Taste von Gleichheitszeichen
def btn_gleichheitszeichen():
    try:
        global Operator
        erhalten_Texte = derText_desEingangs.get()
        Str_erhalten_Texte = str(erhalten_Texte)
        Ergebnis = str(eval(Str_erhalten_Texte))
        btn_entfernen()
        derText_desEingangs.set(Ergebnis)
    except:
        errorMsg('Error')


# =======================================Tasten==============================================

# String fassen
derText_desEingangs = StringVar()

# die Eingabe,um Informationen zu erhalten und das Ergebnis anzeigen
Eintrag_1 = Entry(Fenster, width=37, font=('arial', 14, 'bold'),
                  bd=12, insertwidth=4, bg='powder blue', textvariable=derText_desEingangs)
Eintrag_1.grid(row=5, column=0, rowspan=2, columnspan=7)


# Funktion für die Tasten erstellen
def button(Text, Reihe, Pfeiler, Breite=6, height=2, rowspan=1, columnspan=1, command=None):
    Knopf = Button(master=Fenster, text=Text,
                   highlightbackground="gray", padx=1, pady=1, bd=5, fg='black', font=('arial', 8, 'bold'), width=Breite, height=height, command=command)
    Knopf.grid(row=Reihe, column=Pfeiler,
               rowspan=rowspan, columnspan=columnspan)
    return Knopf


# Taste Nummer sieben
button("7", 7, 0, command=lambda: btn_klick(7))

# Taste Nummer acht
button("8", 7, 1, command=lambda: btn_klick(8))

# Taste Nummer neun
button("9", 7, 2, command=lambda: btn_klick(9))

# Taste Nummer vier
button("4", 8, 0, command=lambda: btn_klick(4))

# Taste Nummer fünf
button("5", 8, 1, command=lambda: btn_klick(5))

# Taste Nummer sechs
button("6", 8, 2, command=lambda: btn_klick(6))

# Taste Nummer eins
button("1", 9, 0, command=lambda: btn_klick(1))

# Taste Nummer zwei
button("2", 9, 1, command=lambda: btn_klick(2))

# Taste Nummer drei
button("3", 9, 2, command=lambda: btn_klick(3))

# Taste plus
button("+", 7, 3, command=lambda: btn_kalkulieren("+"))

# Taste minus
button("-", 8, 3, command=lambda: btn_kalkulieren("-"))

# Taste mal
button("*", 9, 3, command=lambda: btn_kalkulieren("*"))

# Taste durch
button("/", 10, 3, command=lambda: btn_kalkulieren("/"))

# Taste null
button("0", 10, 1, columnspan=1, command=lambda: btn_klick(0))

# Taste löschen
button("C", 10, 2, command=lambda: btn_entfernen())

# Taste Punkt
button(".", 10, 0, command=lambda: btn_kalkulieren("."))

# Taste Gleichung
button("=", 11, 2, command=lambda: btn_gleichheitszeichen())

# Taste Sin
button("sin", 7, 4, command=lambda: btn_klick("sin"))

# Taste Cos
button("cos", 8, 4, command=lambda: btn_klick("cos"))

# Taste Tan
button("tan", 9, 4, command=lambda: btn_klick("tan"))

# Taste tanh
button("tanh", 10, 4, command=lambda: btn_klick("tanh"))

# Taste cosh
button("cosh", 11, 4, command=lambda: btn_klick("cosh"))

# Taste sinh
button("sinh", 11, 5, command=lambda: btn_klick("sinh"))

# Taste Klammer
button("(", 11, 0, command=lambda: btn_klick("("))

# Taste Klammer
button(")", 11, 1, command=lambda: btn_klick(")"))

# Taste factorial
button("factorial", 7, 5, command=lambda: btn_klick("factorial"))

# Taste log
button("log", 8, 5, command=lambda: btn_klick("log"))

# Taste log2
button("log2", 9, 5, command=lambda: btn_klick("log2"))

# Taste log10
button("log10", 10, 5, command=lambda: btn_klick("log10"))

# Taste pi
button("pi", 7, 6, command=lambda: btn_klick("pi"))

# Taste Komma
button(",", 11, 3, command=lambda: btn_klick(","))

# Taste e
button("e", 8, 6, command=lambda: btn_klick("e"))

# Taste fabs
button("fabs", 9, 6, command=lambda: btn_klick("fabs"))

# Taste sqrt
button("sqrt", 10, 6, command=lambda: btn_klick("sqrt"))

# Taste degrees
button("degrees", 11, 6, command=lambda: btn_klick("degrees"))


# ein Loop für das Programm erstellen
Fenster.mainloop()
