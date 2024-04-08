class Employee:
    def __init__(self, name, position, holiday_entitlement, probation_period=False):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period

    def __str__(self):
        probation_info = " a je ve zkušební době." if self.probation_period else "."
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}{probation_info}"

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to. Zbývá ti {self.holiday_entitlement} dní dovolené."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní dovolené."

# Příklad vytvoření a použití objektů třídy Employee
employee1 = Employee("Jan Novák", "Vývojář", 40_000, probation_period=True)
employee2 = Employee("Eva Dvořáková", "Analytička", 45_000)

print(employee1)
print(employee2)
