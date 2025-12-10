# OddOrEven.py
# Program foarte simplu care verifică dacă un număr este par sau impar
# și tratează cazul în care utilizatorul introduce altceva decât un număr.

try:
    # Cerem utilizatorului să introducă un număr
    n = int(input("Introduceți un număr întreg: "))

    # Verificăm dacă este par
    if n % 2 == 0:
        print(f"{n} este par.")
    else:
        print(f"{n} este impar.")

except ValueError:
    # Aceasta eroare apare dacă utilizatorul introduce ceva care nu e număr
    print("Eroare: Te rog introdu un număr întreg valid!")
