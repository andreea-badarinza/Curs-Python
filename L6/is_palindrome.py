def is_palindrome(text):
    # Transformăm toate literele în litere mici
    text = text.lower()

    # Eliminăm spațiile
    text = text.replace(" ", "")

    # Verificăm dacă textul este egal cu inversul lui
    return text == text[::-1]


# Exemplu de test
text = "A man a plan a canal Panama"
print(is_palindrome(text))  # True

