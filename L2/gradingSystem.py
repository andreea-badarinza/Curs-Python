# Program: GradingSystem
# Scop: Cere utilizatorului un scor procentual și afișează nota corespunzătoare.

try:
    # Cerem utilizatorului să introducă scorul
    scor = float(input("Introdu scorul (0-100): "))

    # Verificăm dacă scorul este în intervalul corect
    if scor < 0 or scor > 100:
        print("Eroare: scorul trebuie să fie între 0 și 100.")
    else:
        # Încadrarea scorului în funcție de criterii
        if scor >= 90:
            print("Nota: A")
        elif scor >= 80:
            print("Nota: B")
        elif scor >= 70:
            print("Nota: C")
        elif scor >= 60:
            print("Nota: D")
        else:
            print("Nota: F")

except ValueError:
    # Dacă utilizatorul introduce ceva ce nu e număr
    print("Eroare: te rog introdu un număr valid.")
