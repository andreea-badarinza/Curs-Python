def run_length_encoding(text):
    # Dacă șirul este gol, returnăm șir gol
    if not text:
        return ""

    result = ""
    count = 1  # numără aparițiile caracterului curent

    # Parcurgem șirul de la al doilea caracter
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            # Dacă este același caracter, creștem contorul
            count += 1
        else:
            # Adăugăm caracterul și numărul de apariții
            result += text[i - 1] + str(count)
            count = 1  # resetăm contorul

    # Adăugăm ultimul caracter
    result += text[-1] + str(count)

    return result


# Exemplu de test
text = "aaabbbbcccdde"
print(run_length_encoding(text))  # a3b4c3d2e1
