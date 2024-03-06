# Projdi všechna rodná čísla
for rodne_cislo in rodna_cisla:
    # Rozdělení rodného čísla na datum narození a část identifikující pohlaví
    datum_narozeni = rodne_cislo[:6]
    pohlavi = rodne_cislo[2]
    # Zjištění pohlaví a inkrementace příslušného počítadla
    if pohlavi == "5" or pohlavi == "6":
        pocet_zen += 1
    else:
        pocet_muzu += 1