class Employee:
    # Konstruktor třídy Employee, který inicializuje instance se jménem a pozicí
    def __init__(self, name, position):
        self.name = name  # Jméno zaměstnance
        self.position = position  # Pozice zaměstnance v organizaci

    # Metoda __str__ vracející textový popis instance třídy Employee
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}. "
    

class Manager(Employee):
    # Konstruktor třídy Manager, který rozšiřuje Employee o počet podřízených a auto
    def __init__(self, name, position, subordinates, car):
        super().__init__(name, position)  # Volání konstruktoru nadřazené třídy
        self.subordinates = subordinates  # Počet podřízených, které má manažer
        self.car = car  # Typ auta, které manažer používá

    # Metoda __str__ pro třídu Manager, která doplňuje výstup nadřazené __str__ metody
    def __str__(self):
        return super().__str__() + f"Ma {self.subordinates} podrizenych a auto {self.car}."

# Vytvoření instance třídy Manager a výpis jejího popisu
janina = Manager("Janina", "reditelka kurzu", 55, "Tesla")
print(janina)

# Další instance třídy Employee
# frantisek = Employee("Frantisek", "prodavač")
# jitka = Employee("Jitka", "administrátorka")

# Výpis informací o Františkovi a Jitce
# print(frantisek)
# print(jitka)
