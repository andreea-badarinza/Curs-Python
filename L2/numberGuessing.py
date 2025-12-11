# Program: NumberGuessing
# Scop: Joc simplu în care utilizatorul trebuie să ghicească un număr între 1 și 20.
# Utilizatorul are 5 încercări.

import random  # Importăm modulul random pentru a genera numărul

# Generăm un număr aleator între 1 și 20
numar_secret = random.randint(1, 20)

print("Am ales un număr între 1 și 20. Ai 5 încercări să-l ghicești!")

# Numărul de încercări disponibile
incercari_ramase = 5

# Începem jocul
while incercari_ramase > 0:
    try:
        ghicit = int(input("Introdu numărul tău: "))

        # Verificăm dacă este în intervalul corect
        if ghicit < 1 or ghicit > 20:
            print("Te rog introdu un număr între 1 și 20.")
            continue  # nu consumăm o încercare pentru o valoare invalidă

        # Comparam cu numărul secret
        if ghicit == numar_secret:
            print("Corect! Ai ghicit numărul!")
            break
        elif ghicit > numar_secret:
            print("Prea mare!")
        else:
            print("Prea mic!")

        # Scădem o încercare
        incercari_ramase -= 1
        print(f"Încercări rămase: {incercari_ramase}")

    except ValueError:
        # Dacă utilizatorul introduce altceva decât un număr
        print("Eroare: trebuie să introduci un număr valid.")
        continue

# Dacă utilizatorul nu ghicește în 5 încercări
if incercari_ramase == 0 and ghicit != numar_secret:
    print(f"Ai pierdut! Numărul corect era: {numar_secret}")
