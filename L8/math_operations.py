# math_operations.py
# Acest fișier este un modul care conține funcții matematice de bază

def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b == 0:
        return "Eroare: împărțire la zero"
    return a / b
