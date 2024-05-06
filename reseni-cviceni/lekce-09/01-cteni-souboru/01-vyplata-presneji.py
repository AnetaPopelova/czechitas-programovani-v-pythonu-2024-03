# Otevření souboru a načtení hodin do seznamu
vykaz = []
with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt') as soubor:
    for radek in soubor:
        vykaz.append(int(radek.strip()))


# vykaz = []
# with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt') as soubor:
#     radky = soubor.readlines()
#     for radek in radky:
#         vykaz.append(int(radek.strip()))

# with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt') as soubor:
#     vykaz = list(map(int, soubor.readlines()))


# Výpis seznamu pro kontrolu
print(vykaz)

# Získání hodinové mzdy od uživatele
hodinova_mzda = float(input("Zadejte vaši hodinovou mzdu: "))

# Výpočet celkové výplaty za rok
celkova_vyplata = sum(hodiny * hodinova_mzda for hodiny in vykaz)

# Výpočet průměrné měsíční výplaty
prumerna_vyplata = celkova_vyplata / 12

# Výpis výsledků
print(f"Celková výplata za rok: {celkova_vyplata} Kč")
print(f"Průměrná měsíční výplata: {prumerna_vyplata} Kč")
