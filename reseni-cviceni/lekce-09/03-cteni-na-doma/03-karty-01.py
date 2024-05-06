import random

# Definice barev a hodnot karet
barvy = ['kříže', 'srdce', 'piky', 'káry']
hodnoty = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Vytvoření kompletní sady karet
karty = [f"{hodnota} {barva}" for hodnota in hodnoty for barva in barvy]

# Náhodné vylosování karty
vybrana_karta = random.choice(karty)

# Výpis vylosované karty
print(f"Karta: {vybrana_karta}")
