# Program: FactorialCalculator.py
# Scop: Calculează factorialul unui număr întreg introdus de utilizator

def factorial(n):
    """
    Funcție care calculează factorialul unui număr întreg n
    n: număr întreg nenegativ
    returnează factorialul lui n
    """
    if n == 0 or n == 1:
        return 1
    else:
        rezultat = 1
        for i in range(2, n + 1):
            rezultat *= i
        return rezultat

try:
    # Cerem utilizatorului să introducă un număr întreg
    numar = int(input("Introdu un număr întreg nenegativ: "))

    if numar < 0:
        print("Eroare: factorialul nu este definit pentru numere negative.")
    else:
        # Apelăm funcția factorial și afișăm rezultatul
        print(f"Factorialul lui {numar} este {factorial(numar)}")

except ValueError:
    print("Eroare: trebuie să introduci un număr întreg valid.")
except Exception as e:
    print("A apărut o eroare neașteptată:", e)
