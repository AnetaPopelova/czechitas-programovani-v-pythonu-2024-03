from dataclasses import dataclass

@dataclass
class Package:
    address: str
    weight: float
    state: str

    # def __str__(self):
    #     return f"Balík na adresu: {self.address}, Váha: {self.weight} kg, Stav: {self.state}"

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

# Vytvoření instance třídy Package
package = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
print(package)

# Vytvoření třídy ValuablePackage dědící od Package
@dataclass
class ValuablePackage(Package):
    value: int  # Přidaný atribut pro cenné balíky

    # def __str__(self):
    #     return super().__str__() + f", Hodnota balíku: {self.value} Kč"

# Vytvoření instance třídy ValuablePackage
valuable_package = ValuablePackage("Godrikův důl 47", 3, "nedoručen", 20000)
print(valuable_package)

# Datové třídy automaticky generují metodu __repr__, ale metodu __str__ pro lepší formátovaný výstup musíme definovat explicitně.
