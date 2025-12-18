# LAB 5 - Problema 1
# Functie care calculeaza frecventa fiecarui cuvant dintr-un text
# Ignora majusculele si semnele de punctuatie
# Foloseste dictionare si trateaza exceptiile

import string  # modul pentru semne de punctuatie

def word_frequency(text):
    """
    Primeste un sir de caractere si returneaza un dictionar
    cu frecventa fiecarui cuvant.
    """
    try:
        # Verificam daca inputul este de tip string
        if not isinstance(text, str):
            raise ValueError("Inputul trebuie sa fie un sir de caractere (string).")

        # Transformam textul in litere mici (ignoram majusculele)
        text = text.lower()

        # Eliminam semnele de punctuatie
        for char in string.punctuation:
            text = text.replace(char, "")

        # Impartim textul in cuvinte
        words = text.split()

        # Dictionar pentru frecventa cuvintelor
        frequency = {}

        # Parcurgem lista de cuvinte
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        return frequency

    except Exception as e:
        # Prinde orice eroare neasteptata
        print("A aparut o eroare:", e)
        return {}

# ------------------ Testare ------------------

text = "Ana si Maria au plecat la mare. Maria are rau de mare."
result = word_frequency(text)

print(result)
