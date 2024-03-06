# Seznam rodných čísel pacientů
rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081",
]

# Inicializace počítadel pro muže a ženy
pocet_muzu = 0
pocet_zen = 0

# Inicializace proměnných pro nejstaršího a nejmladšího pacienta
nejstarsi_datum = "999999"
nejmladsi_datum = "000000"

# Projdi všechna rodná čísla
for rodne_cislo in rodna_cisla:
    rok = rodne_cislo[:2]
    mesic = int(rodne_cislo[2:4])
    den = rodne_cislo[4:6]

    # Určení pohlaví a přizpůsobení měsíce
    if mesic > 50:
        pohlavi = "žena"
        pocet_zen += 1
        mesic -= 50
    else:
        pohlavi = "muž"
        pocet_muzu += 1
    
    # Kontrola, zda je měsíc jednociferný, a případné přidání nuly
    if mesic < 10:
        mesic_str = '0' + str(mesic)
    else:
        mesic_str = str(mesic)

    datum_narozeni = rok + mesic_str + den

    # Porovnání s dosavadními nejstarším a nejmladším datem
    if datum_narozeni < nejstarsi_datum:
        nejstarsi_datum = datum_narozeni
    if datum_narozeni > nejmladsi_datum:
        nejmladsi_datum = datum_narozeni

# # Uprav nejstarší a nejmladší datum na formát dd.mm.yy
# nejstarsi_datum = (
#     nejstarsi_datum[4:] + "." + nejstarsi_datum[2:4] + "." + nejstarsi_datum[:2]
# )
# nejmladsi_datum = (
#     nejmladsi_datum[4:] + "." + nejmladsi_datum[2:4] + "." + nejmladsi_datum[:2]
# )

# # Uprav nejstarší a nejmladší datum na formát dd.mm.yy
# nejstarsi_datum = f"{nejstarsi_datum[4:6]}.{nejstarsi_datum[2:4]}.{nejstarsi_datum[:2]}"
# nejmladsi_datum = f"{nejmladsi_datum[4:6]}.{nejmladsi_datum[2:4]}.{nejmladsi_datum[:2]}"

# Vypsání výsledků
print("Počet mužů:", pocet_muzu)
print("Počet žen:", pocet_zen)
print("Nejstarší pacient se narodil:", nejstarsi_datum)
print("Nejmladší pacient se narodil:", nejmladsi_datum)
