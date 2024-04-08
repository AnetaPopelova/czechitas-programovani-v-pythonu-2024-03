class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

# Vytvoření objektů třídy Package
package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 0.5, "nedoručen")

# Seznam balíků
package_list = [package_1, package_2, package_3]

# Vypočet celkové hmotnosti všech balíků
total_weight = 0
for package in package_list:
    total_weight += package.weight
print(f"Celková hmotnost všech balíků je {total_weight} kg.")

# Vypočet celkových nákladů na přepravu
total_delivery_cost = 0
for package in package_list:
    total_delivery_cost += package.delivery_price()
print(f"Celkové náklady na přepravu všech balíků jsou {total_delivery_cost} Kč.")
