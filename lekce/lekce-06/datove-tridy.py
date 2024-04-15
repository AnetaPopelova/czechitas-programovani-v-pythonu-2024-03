from dataclasses import dataclass
from typing import Optional

# Definice třídy Employee pomocí dekorátoru dataclass
@dataclass
class Employee:
    name: str  # Jméno zaměstnance
    position: ... # Pozice zaměstnance v organizaci
    holiday: Optional[int] = None  # Počet dnů dovolené, volitelný atribut s výchozí hodnotou None

    def __str__(self):
        # Metoda pro přizpůsobený tiskový výstup objektu třídy Employee
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

# Vytvoření instance třídy Employee
denisa = Employee("Denisa", "programátorka")
print(denisa)  # Výpis informací o Denisě

# Definice třídy Manager, která je odvozena od třídy Employee
@dataclass
class Manager(Employee):
    subordinates: int  # Počet podřízených
    car: str  # Značka nebo model auta, které manažer používá

    def __str__(self):
        # Metoda pro přizpůsobený tiskový výstup objektu třídy Manager
        # Zavolá metodu __str__() z mateřské třídy a přidá specifické informace pro manažera
        return super().__str__() + f"Má {self.subordinates} podřízených a auto {self.car}."

# Vytvoření instance třídy Manager
olga = Manager("Olga", "vedoucí", 53, "modré")
print(olga)  # Výpis informací o Olze

# Kontrola, zda má objekt manažera atribut 'car'
if hasattr(olga, "car"):
    print(olga.car)  # Výpis auta manažera

# Příklad použití getattr pro získání atributu 'car' s výchozí hodnotou "Není auto", pokud atribut neexistuje
print(getattr(denisa, "car", "Není auto"))

# Denisa nemá atribut 'car'
print(hasattr(denisa, "car"))  # Vrátí False, protože Denisa nemá atribut 'car'
