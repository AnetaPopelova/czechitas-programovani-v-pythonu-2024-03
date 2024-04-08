from dataclasses import dataclass

@dataclass
class Package:
    address: str
    weight: float
    state: str  # Přidán stav balíku

@dataclass
class ValuablePackage(Package):
    value: int  # Přidaný atribut pro cenné balíky

# Vytvoření balíků s aktualizovaným stavem
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "doručen", 5500)  # Tento balík byl již doručen

package_list = [package_1, package_2, package_3]

# Vypočet celkové hodnoty nedoručených cenných balíků
total_value = 0
for package in package_list:
    if isinstance(package, ValuablePackage) and getattr(package, 'state', '') == 'nedoručen':
        total_value += getattr(package, 'value', 0)

print(f"Celková hodnota nedoručených cenných balíků v autě je: {total_value} Kč.")
