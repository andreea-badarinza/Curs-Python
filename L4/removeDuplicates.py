# RemoveDuplicates.py
# Program care:
# 1. Citeste de la tastatura o lista de numere separate prin virgula
# 2. Converteste inputul intr-o lista de numere intregi
# 3. Inlatura valorile duplicate
# 4. Pastreaza ordinea in care valorile apar prima data
# 5. Afiseaza lista cu valori unice
# Sunt tratate toate erorile posibile

try:
    # Citim inputul de la tastatura
    user_input = input("Introduceti o lista de numere separate prin virgula: ")

    # Verificam daca inputul este gol
    if not user_input.strip():
        raise ValueError("Nu ati introdus niciun numar.")

    # Spargem inputul dupa virgula
    numbers_str = user_input.split(",")

    # Convertim string-urile in numere intregi
    numbers = [int(num.strip()) for num in numbers_str]

    # Lista in care vom pastra valorile unice
    unique_numbers = []

    # Parcurgem lista originala
    for num in numbers:
        # Daca numarul nu este deja in lista de valori unice, il adaugam
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Afisam rezultatul
    print("Lista fara duplicate este:", unique_numbers)

except ValueError as ve:
    # Apare daca inputul nu este valid (litere, input gol etc.)
    print("Eroare de valoare:", ve)

except Exception as e:
    # Prinde orice alta eroare neasteptata
    print("A aparut o eroare neasteptata:", e)
