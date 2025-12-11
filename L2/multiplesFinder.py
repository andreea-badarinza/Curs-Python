# Program: MultiplesFinder
# Scop: Cere două numere x și y și afișează toate multiplurile lui x mai mici decât y.

try:
    # Cerem utilizatorului numerele
    x = int(input("Introdu valoarea lui x: "))
    y = int(input("Introdu valoarea lui y: "))

    # Verificăm dacă x este 0 (nu există multipli ai lui 0)
    if x == 0:
        print("Eroare: x nu poate fi 0, deoarece nu există multipli ai lui 0.")
    else:
        print(f"Multiplii lui {x} mai mici decât {y} sunt:")

        # Găsim și afișăm multiplii
        multiple = x
        while multiple < y:
            print(multiple)
            multiple += x  # trecem la următorul multiplu

except ValueError:
    # Dacă utilizatorul introduce ceva ce nu e număr
    print("Eroare: te rog introdu numere valide (numere întregi).")
