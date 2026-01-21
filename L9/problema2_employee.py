# Definim clasa de bază Employee
# Aceasta reprezintă un angajat simplu
class Employee:

    # Constructorul clasei Employee
    def __init__(self, name, salary):
        self.name = name  # numele angajatului
        self.salary = salary  # salariul angajatului

    # Metodă care returnează detalii despre angajat
    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


# Definim clasa Manager
# Aceasta moștenește clasa Employee (inheritance)
class Manager(Employee):

    # Constructorul clasei Manager
    def __init__(self, name, salary, department):
        # Apelăm constructorul clasei părinte (Employee)
        super().__init__(name, salary)
        self.department = department  # departamentul managerului

    # Suprascriem metoda get_details() (method overriding)
    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


# Creăm un obiect de tip Employee
emp = Employee("John", 3000)

# Creăm un obiect de tip Manager
mgr = Manager("Alice", 5000, "IT")

# Afișăm detaliile pentru fiecare obiect
print(emp.get_details())
print(mgr.get_details())
