class Package:
    def __init__(self, address, weight, state="nedoručen"):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address}, váha {self.weight} kg, je ve stavu {self.state}."

    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen."
        else:
            self.state = "doručen"
            return "Doručení uloženo."

# Vytvoření a testování objektů třídy Package
package1 = Package("Václavské náměstí 12, Praha", 0.5)
package2 = Package("Příkopy 23, Brno", 1.2)

print(package1)
print(package2)

# Testování doručení
print(package1.deliver())
print(package1.deliver())  # Zkusíme doručit znovu

print(package2.deliver())
