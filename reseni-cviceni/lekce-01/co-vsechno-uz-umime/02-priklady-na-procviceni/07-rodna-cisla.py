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
    # Rozdělení rodného čísla na datum narození a část identifikující pohlaví
    datum_narozeni = rodne_cislo[:6]
    pohlavi = rodne_cislo[7]

    # Zjištění pohlaví a inkrementace příslušného počítadla
    if pohlavi == "5":
        pocet_zen += 1
    else:
        pocet_muzu += 1

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
