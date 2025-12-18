# LAB 5 - Problema 2
# Functie care gaseste perechi unice de numere
# a caror suma este egala cu valoarea tinta
# Perechile sunt returnate ca tupluri (a, b), unde a <= b
# Sunt tratate toate erorile posibile

def unique_pair_sum(numbers, target):
    """
    Primeste o lista de numere intregi si o valoare tinta.
    Returneaza un set de perechi unice (a, b) cu a <= b,
    pentru care a + b == target.
    """
    try:
        # Verificam daca numbers este o lista
        if not isinstance(numbers, list):
            raise ValueError("Primul parametru trebuie sa fie o lista.")

        # Verificam daca target este un numar intreg
        if not isinstance(target, int):
            raise ValueError("Valoarea tinta trebuie sa fie un numar intreg.")

        # Verificam daca toate elementele din lista sunt numere intregi
        for num in numbers:
            if not isinstance(num, int):
                raise ValueError("Lista trebuie sa contina doar numere intregi.")

        # Set pentru a pastra perechile unice
        pairs = set()

        # Set pentru a memora numerele deja vazute
        seen = set()

        # Parcurgem lista de numere
        for num in numbers:
            complement = target - num

            # Daca complementul a fost vazut anterior,
            # putem forma o pereche valida
            if complement in seen:
                # Ne asiguram ca a <= b
                a = min(num, complement)
                b = max(num, complement)

                # Adaugam perechea in set (evita duplicatele)
                pairs.add((a, b))

            # Adaugam numarul curent in setul seen
            seen.add(num)

        return pairs

    except Exception as e:
        # Prinde orice eroare neasteptata
        print("A aparut o eroare:", e)
        return set()

# ------------------ Testare ------------------

numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7

result = unique_pair_sum(numbers, target)
print(result)
