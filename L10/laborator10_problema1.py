# laborator10_problema1.py
# Problema 1 - Împărțirea a două numere cu tratarea excepției

def imparte(a, b):
    try:
        rezultat = a / b
        return rezultat
    except ZeroDivisionError:
        print("Eroare: Împărțirea la zero nu este permisă.")
        return None

# Test
if __name__ == "__main__":
    print("Test Problema 1")
    num1 = 10
    num2 = 0
    print("Rezultat:", imparte(num1, num2))
