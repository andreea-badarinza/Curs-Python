# LAB 5 - Problema 3
# Functie care construieste un index invers
# Asociaza fiecarui cuvant unic un set de indici
# ai documentelor in care apare acel cuvant
# Sunt tratate toate erorile posibile

import string

def inverted_index(documents):
    """
    Primeste o lista de siruri de caractere (documente)
    si returneaza un dictionar:
    cheie   -> cuvant unic
    valoare -> set de indici ai documentelor in care apare
    """
    try:
        # Verificam daca documents este o lista
        if not isinstance(documents, list):
            raise ValueError("Inputul trebuie sa fie o lista de documente.")

        # Dictionar pentru indexul invers
        index = {}

        # Parcurgem documentele impreuna cu indexul lor
        for doc_index, document in enumerate(documents):

            # Verificam daca fiecare document este string
            if not isinstance(document, str):
                raise ValueError("Fiecare document trebuie sa fie un sir de caractere.")

            # Transformam documentul in litere mici
            text = document.lower()

            # Eliminam semnele de punctuatie
            for char in string.punctuation:
                text = text.replace(char, "")

            # Spargem documentul in cuvinte
            words = text.split()

            # Parcurgem fiecare cuvant din document
            for word in words:
                # Daca cuvantul nu exista in dictionar, il initializam cu set gol
                if word not in index:
                    index[word] = set()

                # Adaugam indexul documentului in set
                index[word].add(doc_index)

        return index

    except Exception as e:
        # Prinde orice eroare neasteptata
        print("A aparut o eroare:", e)
        return {}

# ------------------ Testare ------------------

documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și câinele s-au jucat împreună"
]

result = inverted_index(documents)

# Afisam rezultatul
for word, doc_ids in result.items():
    print(f"{word}: {doc_ids}")
