from dataclasses import dataclass

@dataclass
class Package:
    address: str
    weight: float
    state: str

@dataclass
class ValuablePackage(Package):
    value: int

# Vytvoření balíků
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

# Vypočet celkové hodnoty cenných balíků
total_value = 0
for package in package_list:
    
    if isinstance(package, ValuablePackage): # Zkontroluj, zda je balík instance třídy ValuablePackage
    # if hasattr(package, 'value'): # Zkontroluj, zda má balík atribut 'value'
        value = getattr(package, 'value', 0)
        # Přičti hodnotu balíku k celkové hodnotě
        total_value += value

print(f"Celková hodnota balíků v autě je: {total_value} Kč.")
