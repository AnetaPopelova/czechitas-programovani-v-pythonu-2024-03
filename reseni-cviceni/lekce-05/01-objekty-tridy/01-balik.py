class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

# Vytvoření objektů třídy Package
package1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
package2 = Package("Petrská 113/6, Praha", 15, "doručen")

# Vypsání informací o balících
print(package1.get_info())
print(package2.get_info())

# Vypsání ceny přepravy pro každý balík
print(f"Cena přepravy pro první balík je {package1.delivery_price()} Kč.")
print(f"Cena přepravy pro druhý balík je {package2.delivery_price()} Kč.")
