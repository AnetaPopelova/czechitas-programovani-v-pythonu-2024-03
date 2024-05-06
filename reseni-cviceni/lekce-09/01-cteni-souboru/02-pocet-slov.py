# Otevření souboru a načtení řádků do seznamu
seznam_radku = []
with open('reseni-cviceni/lekce-09/01-cteni-souboru/praha.txt', 'r', encoding='utf-8') as soubor:
    seznam_radku = soubor.readlines()

# Analýza počtu slov na řádcích a výpis
celkovy_pocet_slov = 0
print("Počet slov na řádku:")
for radek in seznam_radku:
    slova = radek.split()
    pocet_slov = len(slova)
    print(pocet_slov)
    celkovy_pocet_slov += pocet_slov

# Výpis celkového počtu slov
print(f"Celkový počet slov v dokumentu: {celkovy_pocet_slov}")
