# TupleElementSearch.py
# Program care:
# 1. Citeste valori separate prin virgula de la tastatura
# 2. Creeaza o tupla
# 3. Cauta o valoare introdusa de utilizator in tupla
# 4. Afiseaza daca valoarea exista si indexul acesteia
# Sunt tratate toate erorile posibile

try:
    # Citim inputul pentru tupla
    user_input = input("Introduceti valorile pentru tupla (separate prin virgula): ")

    # Verificam daca inputul este gol
    if not user_input.strip():
        raise ValueError("Nu ati introdus nicio valoare pentru tupla.")

    # Spargem inputul dupa virgula
    elements_str = user_input.split(",")

    # Convertim valorile in numere intregi
    elements_list = [int(el.strip()) for el in elements_str]

    # Cream tupla din lista
    elements_tuple = tuple(elements_list)

    # Afisam tupla
    print("Tupla este:", elements_tuple)

    # Citim valoarea cautata
    search_value = int(input("Introduceti valoarea de cautat: "))

    # Verificam daca valoarea se afla in tupla
    if search_value in elements_tuple:
        # index() returneaza prima pozitie unde apare valoarea
        index = elements_tuple.index(search_value)
        print(f"{search_value} se regaseste in tupla la indexul {index}.")
    else:
        print(f"{search_value} NU se regaseste in tupla.")

except ValueError as ve:
    # Apare daca inputul nu este valid sau conversia la int esueaza
    print("Eroare de valoare:", ve)

except Exception as e:
    # Prinde orice alta eroare neasteptata
    print("A aparut o eroare neasteptata:", e)
