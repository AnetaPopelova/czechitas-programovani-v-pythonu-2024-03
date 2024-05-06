import random

# Funkce pro načtení karet ze souboru
def nacti_karty(soubor):
    with open(soubor, 'r') as file:
        karty = [line.strip() for line in file]
    return karty

# Mapování hodnot karet na jejich numerické ekvivalenty pro výpočet
hodnoty_karet = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'kluk': 10, 'dáma': 10, 'král': 10, 'eso': 1
}
# Načtení karet ze souboru
karty = nacti_karty('reseni-cviceni/lekce-09/03-cteni-na-doma/karty.txt')

# Zamíchání karet
random.shuffle(karty)

# Vylosování 4 karet
vybrane_karty = karty[:4]

# Výpočet celkové hodnoty vybraných karet
celkova_hodnota = sum(hodnoty_karet[karta.split()[0]] for karta in vybrane_karty)

# Výpis vylosovaných karet a celkové hodnoty
print("Vylosované karty:")
print(vybrane_karty)
print(f"Celková hodnota karet: {celkova_hodnota}")
