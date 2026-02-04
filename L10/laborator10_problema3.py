# laborator10_problema3.py
# Problema 3 - Sistem simplu de gestionare inventar

inventar = {}

def adauga_produs(nume, cantitate):
    try:
        cantitate = int(cantitate)
        if nume in inventar:
            inventar[nume] += cantitate
        else:
            inventar[nume] = cantitate
        print(f"Produsul '{nume}' a fost adăugat/actualizat. Cantitate: {inventar[nume]}")
    except ValueError:
        print("Eroare: Cantitatea trebuie să fie un număr întreg.")

def cauta_produs(nume):
    if nume in inventar:
        print(f"Produs: {nume}, Cantitate: {inventar[nume]}")
    else:
        print(f"Eroare: Produsul '{nume}' nu există.")

def actualizeaza_cantitate(nume, cantitate_noua):
    try:
        cantitate_noua = int(cantitate_noua)
        if nume in inventar:
            inventar[nume] = cantitate_noua
            print(f"Produsul '{nume}' a fost actualizat. Noua cantitate: {cantitate_noua}")
        else:
            print(f"Eroare: Produsul '{nume}' nu există.")
    except ValueError:
        print("Eroare: Cantitatea trebuie să fie un număr întreg.")

# Interfață simplă
if __name__ == "__main__":
    while True:
        print("\n1. Adaugă produs")
        print("2. Caută produs")
        print("3. Actualizează cantitate")
        print("4. Ieșire")
        optiune = input("Alege opțiunea: ")

        if optiune == "1":
            nume = input("Nume produs: ")
            cant = input("Cantitate: ")
            adauga_produs(nume, cant)
        elif optiune == "2":
            nume = input("Nume produs: ")
            cauta_produs(nume)
        elif optiune == "3":
            nume = input("Nume produs: ")
            cant = input("Noua cantitate: ")
            actualizeaza_cantitate(nume, cant)
        elif optiune == "4":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Alege între 1-4.")
