class Package:
    def __init__(self, address, weight, state="nedoručen"):
        self.address = address
        self.weight = weight
        self._state = state

    def __str__(self):
        return f"Balík na adresu {self.address}, váha {self.weight} kg, je ve stavu {self._state}."
    
    def deliver(self):
        if self._state == "doručen":
            return "Balík již byl doručen."
        else:
            self._state = "doručen"
            return "Doručení uloženo."

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f", hodnota balíku: {self.value} Kč."

# Vytvoření objektů třídy Package a ValuablePackage
ordinary_package = Package("Godrikův důl 47", 3, "nedoručen")
valuable_package = ValuablePackage("Grimmauldovo náměstí 11", 15, "nedoručen", 20_000)

# Vypsání informací o obou balících
print(ordinary_package)
print(valuable_package)
