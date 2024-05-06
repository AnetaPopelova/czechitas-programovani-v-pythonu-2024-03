# Otevření souboru a načtení hodin do seznamu
vykaz = []
with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt', 'r') as soubor:
    for radek in soubor:
        vykaz.append(int(radek.strip()))

# Získání hodinové mzdy od uživatele
hodinova_mzda = float(input("Zadejte vaši hodinovou mzdu: "))

# Výpočet výplaty za každý měsíc
výplaty = [hodiny * hodinova_mzda for hodiny in vykaz]

# Výpis výplat za každý měsíc na terminál
for index, vyplata in enumerate(výplaty, start=1):
    print(f"Měsíc {index}: {vyplata} Kč")

# Zápis výplat do souboru
with open('vypis_vyplat.txt', 'w') as soubor:
    for index, vyplata in enumerate(výplaty, start=1):
        soubor.write(f"Měsíc {index}: {vyplata} Kč\n")
