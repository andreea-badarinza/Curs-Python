def reverse_words(sentence):
    # Eliminăm spațiile suplimentare și împărțim propoziția în cuvinte
    words = sentence.split()

    # Inversăm lista de cuvinte
    reversed_words = words[::-1]

    # Refacem propoziția din cuvintele inversate
    result = " ".join(reversed_words)

    return result


# Exemplu de test
sentence = "soricel un cu joaca se pisica"
print(reverse_words(sentence))  # pisica se joaca cu un soricel
