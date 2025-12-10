# Verificare dacă un număr este prim - 3


# Cerem utilizatorului un număr întreg
while True:
    try:
        n = int(input("Introduceți un număr: "))
        break
    except ValueError:
        print("Te rog introduce un număr întreg valid.\n")

# Presupunem că numărul este prim la început
este_prim = True

# Numerele mai mici sau egale cu 1 NU sunt prime
if n <= 1:
    este_prim = False
else:
    # Verificăm dacă n are vreun divizor între 2 și n-1
    for i in range(2, n):
        if n % i == 0:
            este_prim = False
            break  # oprim căutarea, deja știm că NU e prim

# Afișăm rezultatul
if este_prim:
    print(f"{n} este un număr prim.")
else:
    print(f"{n} NU este un număr prim.")
