# Původní seznam čísel
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializace seznamů pro sudá a lichá čísla
suda_cisla = []
licha_cisla = []

# Projdi všechna čísla v původním seznamu
for cislo in cisla:
    # Pokud je číslo sudé, přidej ho do seznamu s sudými čísly
    if cislo % 2 == 0:
        suda_cisla.append(cislo)
    # Pokud je číslo liché, přidej ho do seznamu s lichými čísly
    else:
        licha_cisla.append(cislo)

# Vypsání nových seznamů se sudými a lichými čísly
print("Seznam sudých čísel:", suda_cisla)
print("Seznam lichých čísel:", licha_cisla)
