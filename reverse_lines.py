def reverse_lines(input_file, output_file):
    # Deschidem fișierul de intrare în modul citire
    with open(input_file, "r", encoding="utf-8") as file:
        # Citim toate liniile din fișier
        lines = file.readlines()

    # Deschidem fișierul de ieșire în modul scriere
    with open(output_file, "w", encoding="utf-8") as file:
        # Parcurgem fiecare linie din fișierul de intrare
        for line in lines:
            # Eliminăm caracterul de linie nouă (\n)
            line = line.strip()

            # Inversăm caracterele din linie
            reversed_line = line[::-1]

            # Scriem linia inversată în fișierul de ieșire
            file.write(reversed_line + "\n")


# Apelarea funcției
reverse_lines("input.txt", "output.txt")

print("Fișierul output.txt a fost creat cu succes!")
