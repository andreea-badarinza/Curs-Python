# Definim clasa BankAccount
# Această clasă reprezintă un cont bancar
class BankAccount:

    # Constructorul clasei
    # Se apelează automat când creăm un obiect BankAccount
    def __init__(self, initial_balance):
        # _balance este un atribut privat (encapsulation)
        # Nu ar trebui accesat direct din afara clasei
        self._balance = initial_balance

    # Metodă pentru depunerea banilor în cont
    def deposit(self, amount):
        # Verificăm dacă suma este pozitivă
        if amount > 0:
            self._balance += amount  # adăugăm suma la sold
            print("Depunere reușită")

    # Metodă pentru retragerea banilor din cont
    def withdraw(self, amount):
        # Verificăm dacă există suficienți bani în cont
        if amount <= self._balance:
            self._balance -= amount  # scădem suma din sold
            print("Retragere reușită")
        else:
            # Mesaj afișat dacă nu sunt bani suficienți
            print("Fonduri insuficiente")

    # Metodă pentru obținerea soldului curent
    def get_balance(self):
        return self._balance


# Creăm un obiect de tip BankAccount cu sold inițial 1000
account = BankAccount(1000)

# Depunem 500 în cont
account.deposit(500)

# Retragem 300 din cont
account.withdraw(300)

# Afișăm soldul final
print("Sold:", account.get_balance())
