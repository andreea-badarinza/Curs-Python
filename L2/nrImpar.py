# Program: Numere Impare până la n
# Scop: Citește un număr n de la tastatură și afișează toate numerele impare până la n.

try:
    # Citim valoarea lui n
    n = int(input("Introdu un număr n: "))

    # Verificăm dacă n este pozitiv
    if n <= 0:
        print("Te rog introdu un număr mai mare decât 0.")
    else:
        print(f"Numerele impare până la {n} sunt:")

        # Parcurgem numerele de la 1 la n și afișăm doar imparele
        for i in range(1, n + 1):
            if i % 2 == 1:   # condiție pentru număr impar
                print(i)

except ValueError:
    print("Eroare: te rog introdu un număr întreg valid.")
