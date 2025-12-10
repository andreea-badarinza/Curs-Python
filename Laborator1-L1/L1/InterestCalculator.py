# InterestCalculator.py
# Program care calculează dobânda simplă
# Include verificări de bază pentru introducerea numerelor

# Funcție simplă care cere un număr de tip float și repetă întrebarea dacă utilizatorul greșește
def get_float_input(message):
    while True:
        try:
            value = float(input(message))
            return value   # ieșim din while dacă utilizatorul introduce un număr valid
        except ValueError:
            print(" Te rog introdu un număr valid.\n")  # mesaj de eroare

# Cerem utilizatorului datele necesare cu verificări
principal = get_float_input("Introduceți principalul (suma împrumutată): ")
rate = get_float_input("Introduceți rata anuală a dobânzii (ex: 5, 6, 10): ")
time = get_float_input("Introduceți timpul în ani: ")

# Formula dobânzii simple
interest = (principal * rate * time) / 100

# Afișăm rezultatul
print(f"\nDobânda totală este: {interest}")
