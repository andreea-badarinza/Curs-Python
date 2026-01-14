def filter_lines(input_file, output_file, keyword):
    # Deschidem fișierul de intrare în modul citire
    with open(input_file, "r", encoding="utf-8") as file:
        # Citim fiecare linie pe rând
        lines = file.readlines()

    # Deschidem fișierul de ieșire în modul scriere
    with open(output_file, "w", encoding="utf-8") as file:
        # Parcurgem fiecare linie
        for line in lines:
            # Verificăm dacă cuvântul cheie există în linie
            if keyword in line:
                # Dacă da, scriem linia în fișierul de ieșire
                file.write(line)


# Apelarea funcției
filter_lines("input.txt", "filtered.txt", "Python")

print("Fișierul filtered.txt a fost creat cu succes!")
