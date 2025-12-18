# MaximumMinimum.py
# Program care citeste o lista de numere separate prin virgula,
# o converteste intr-o lista de numere intregi
# si afiseaza valoarea maxima si minima.
# Sunt tratate toate erorile posibile.

try:
    # Citim inputul de la tastatura
    user_input = input("Introduceti o lista de numere separate prin virgula: ")

    # Verificam daca utilizatorul a introdus ceva
    if not user_input.strip():
        raise ValueError("Nu ati introdus niciun numar.")

    # Spargem textul dupa virgula (rezulta o lista de string-uri)
    numbers_str = user_input.split(",")

    # Convertim lista de string-uri intr-o lista de intregi
    numbers = [int(num.strip()) for num in numbers_str]

    # Verificam daca lista contine elemente
    if len(numbers) == 0:
        raise ValueError("Lista este goala.")

    # Calculam maximul si minimul
    maximum = max(numbers)
    minimum = min(numbers)

    # Afisam rezultatele
    print("Lista de numere este:", numbers)
    print("Valoarea maxima este:", maximum)
    print("Valoarea minima este:", minimum)

except ValueError as ve:
    # Apare daca inputul nu poate fi convertit in int
    print("Eroare de valoare:", ve)

except Exception as e:
    # Prinde orice alta eroare neasteptata
    print("A aparut o eroare neasteptata:", e)
