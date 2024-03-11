# Import knihovny math pro matematické funkce
import math
# Import knihovny statistics pro statistické funkce
import statistics

# Inicializace proměnné s plovoucí desetinnou čárkou
cislo = 3.14

# Použití funkce floor() z knihovny math pro zaokrouhlení čísla dolů
print(math.floor(cislo))
# Následující řádek je zakomentovaný, jelikož pro použití funkce floor() je nutné specifikovat knihovnu (math.floor()), jinak by došlo k chybě
# print(floor(cislo))

# Použití funkce ceil() z knihovny math pro zaokrouhlení čísla nahoru
print(math.ceil(cislo))

# Výpočet a výpis průměru ze seznamu čísel [1, 10] pomocí funkce mean() z knihovny statistics
print(statistics.mean([1, 10]))
