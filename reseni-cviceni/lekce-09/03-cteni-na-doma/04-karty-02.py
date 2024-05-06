import random

# Definice barev a hodnot karet
barvy = ['kříže', 'srdce', 'piky', 'káry']
hodnoty = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Mapování hodnot karet na jejich numerické ekvivalenty pro výpočet
hodnoty_karet = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# Vytvoření kompletní sady karet
karty = [f"{hodnota} {barva}" for hodnota in hodnoty for barva in barvy]

# Náhodné vylosování 4 karet
vybrane_karty = random.sample(karty, 4)

# Výpočet celkové hodnoty vybraných karet
celkova_hodnota = sum(hodnoty_karet[karta.split()[0]] for karta in vybrane_karty)

# Výpis vylosovaných karet
print("Vylosované karty:")
for karta in vybrane_karty:
    print(karta)

# Výpis celkové hodnoty
print(f"Celková hodnota karet: {celkova_hodnota}")
