# Program: PalindromeChecker fără funcție
# Scop: Verifică dacă un cuvânt introdus de utilizator este palindrom.

try:
    cuvant = input("Introdu un cuvânt: ").strip()

    # Verifică dacă cuvântul nu este gol și conține doar litere
    if len(cuvant) == 0:
        print("Eroare: trebuie să introduci un cuvânt valid.")
    elif not cuvant.isalpha():
        print("Eroare: cuvântul trebuie să conțină doar litere.")
    else:
        cuvant_mic = cuvant.lower()
        cuvant_invers = cuvant_mic[::-1]

        if cuvant_mic == cuvant_invers:
            print(f"Cuvântul '{cuvant}' este palindrom.")
        else:
            print(f"Cuvântul '{cuvant}' NU este palindrom.")

except Exception as e:
    print("A apărut o eroare neașteptată:", e)
