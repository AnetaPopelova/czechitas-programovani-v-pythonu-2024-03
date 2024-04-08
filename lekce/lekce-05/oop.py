class Employee:
    # Konstruktor třídy, inicializuje zaměstnance s danými atributy
    def __init__(self, name, position, holiday_entitlement, gross_salary):
        self.name = name  # jméno zaměstnance
        self.position = position  # pozice zaměstnance
        self._holiday_entitlement = holiday_entitlement  # počet dní dovolené
        self.gross_salary = gross_salary  # hrubý plat

    # Speciální metoda pro reprezentaci objektu jako řetězec
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position} :-)."

    # Metoda pro čerpání dovolené, odečítá dny z nároku
    def take_holiday(self, days):
        if self._holiday_entitlement >= days:
            self._holiday_entitlement -= days
            return "Užij si to."
        else:
            return f"Bohužel, už nemáš nárok, zbývá ti jen {self._holiday_entitlement} dní dovolené."

    # Property pro výpočet čisté mzdy (předpokládá paušální daň 15%)
    @property
    def net_salary(self):
        return self.gross_salary * (1 - 0.15)  # Vypočítá a vrátí čistou mzdu

# Vytvoření instance zaměstnance Františka
frantisek = Employee("Frantisek", "prodavač", 9, 120000)
# Výpis informací o Františkovi pomocí metody __str__
print(frantisek)

# Vytvoření instance zaměstnance Jitky
jitka = Employee("Jitka", "administrátorka", 25, 150000)
# Výpis informací o Jitce
print(jitka)

# František si bere 5 dní dovolené
print(frantisek.take_holiday(5))
# František se pokouší vzít dalších 35 dní, ale nemá dostatek nároku
print(frantisek.take_holiday(35))

# Přímá manipulace s privátním atributem (by se mělo vyhnout)
frantisek._holiday_entitlement = 0

# Výpočet a výpis čisté mzdy Františka
print(frantisek.net_salary)
