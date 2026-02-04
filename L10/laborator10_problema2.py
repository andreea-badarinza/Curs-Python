# laborator10_problema2.py
# Problema 2 - Citirea unui fișier și calcularea sumei numerelor

def suma_din_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, 'r') as f:
            for linie in f:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print(f"Atenție: '{linie.strip()}' nu este un număr valid și va fi ignorat.")
        return suma
    except FileNotFoundError:
        print("Eroare: Fișierul nu există.")
        return None
    except IOError:
        print("Eroare la citirea fișierului.")
        return None

# Test
if __name__ == "__main__":
    print("Test Problema 2")
    fisier = "numere.txt"  # Creează acest fișier în proiect
    print("Suma numerelor:", suma_din_fisier(fisier))
