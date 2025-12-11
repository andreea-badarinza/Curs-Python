# Program: DistanceBetweenPoints.py
# Scop: Calculează distanța euclidiană între două puncte (x1, y1) și (x2, y2)

import math  # Importăm modulul math pentru funcția sqrt

def distance(x1, y1, x2, y2):
    """
    Funcție care calculează distanța euclidiană între două puncte
    (x1, y1) și (x2, y2)
    returnează distanța ca număr real
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

try:
    # Cerem utilizatorului să introducă coordonatele celor două puncte
    x1 = float(input("Introdu coordonata x a primului punct: "))
    y1 = float(input("Introdu coordonata y a primului punct: "))
    x2 = float(input("Introdu coordonata x a celui de-al doilea punct: "))
    y2 = float(input("Introdu coordonata y a celui de-al doilea punct: "))

    # Calculăm distanța folosind funcția definită mai sus
    dist = distance(x1, y1, x2, y2)
    print(f"Distanța dintre puncte este: {dist:.2f}")

except ValueError:
    print("Eroare: te rog să introduci un număr valid pentru coordonate.")
except Exception as e:
    print("A apărut o eroare neașteptată:", e)
