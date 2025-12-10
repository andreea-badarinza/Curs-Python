while True:
    try:
        celsius_input = input("Introduceți temperatura în grade Celsius: ")
        celsius = float(celsius_input)      # încearcă transformarea în număr
        break                               # dacă reușește, ieșim din while
    except ValueError:
        print("Eroare: introduceți un număr valid!\n")

fahrenheit = celsius * 9/5 + 32
print("Temperatura în Fahrenheit este:", fahrenheit)
