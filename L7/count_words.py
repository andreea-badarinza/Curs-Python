def count_words_in_file(filename):
    # Deschidem fișierul în modul citire ("r")
    with open(filename, "r", encoding="utf-8") as file:
        # Citim tot conținutul fișierului
        content = file.read()

    # Împărțim textul în cuvinte (spațiile sunt eliminate automat)
    words = content.split()

    # Returnăm numărul total de cuvinte
    return len(words)


# Apelarea funcției
result = count_words_in_file("example.txt")

# Afișăm rezultatul
print(result)
