from dataclasses import dataclass

@dataclass
class Driver:
    name: str
    phone_number: str

@dataclass
class Package:
    address: str
    weight: float
    state: str
    driver: Driver  # Nový atribut pro uchování informace o řidiči

    def send_message(self):
        message = f"Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: {self.driver.phone_number}"
        print(message)

@dataclass
class ValuablePackage(Package):
    value: int  # Přidaný atribut pro cenné balíky

    def __init__(self, address, weight, state, value, driver):
        super().__init__(address, weight, state, driver)  # Předání řidiče rodičovské třídě
        self.value = value

# Vytvoření řidiče
driver1 = Driver("Jan Novák", "+420123456789")

# Vytvoření balíků
package = Package("Grimmauldovo náměstí 11", 1.5, "nedoručen", driver1)
valuable_package = ValuablePackage("Vydrník svatého Drába 13", 2.0, "nedoručen", 20000, driver1)

# Odeslání SMS zprávy
package.send_message()
valuable_package.send_message()
