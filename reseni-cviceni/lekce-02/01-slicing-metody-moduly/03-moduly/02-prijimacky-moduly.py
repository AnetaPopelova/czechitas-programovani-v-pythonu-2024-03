import statistics

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

# Vytvoření prázdného seznamu pro známky z vybraných předmětů
vybrane_znamky = []

# Cyklus pro vložení známek z vybraných předmětů do nového seznamu
for predmet, znamka in school_report:
    if predmet in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
        vybrane_znamky.append(znamka)

# Výpočet průměru studenta
prumer = statistics.mean(vybrane_znamky)

# Získání nejlepší a nejhorší známky z vybraných předmětů
nejlepsi_znamka = max(vybrane_znamky)
nejhorsi_znamka = min(vybrane_znamky)

print("Průměr studenta:", prumer)
print("Nejlepší známka:", nejlepsi_znamka)
print("Nejhorší známka:", nejhorsi_znamka)
