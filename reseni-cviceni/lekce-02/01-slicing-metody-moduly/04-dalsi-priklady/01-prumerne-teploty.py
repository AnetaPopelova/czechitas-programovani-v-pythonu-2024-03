# Vytvoření seznamu seznamů pro reprezentaci tabulky
radky = [
    [2001, 7.8],
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2]
]

# Vytvoření seznamu sloupců z tabulky
sloupce = [
    [radka[0] for radka in radky],  # Seznam roků
    [radka[1] for radka in radky]   # Seznam teplot
]

# Získání teploty na třetím řádku tabulky
teplota_treti_radka = radky[2][1]
print("Teplota na třetím řádku:", teplota_treti_radka)

# Získání roku na pátém řádku tabulky
rok_paty_radka = radky[4][0]
print("Rok na pátém řádku:", rok_paty_radka)

# Získání posledního řádku tabulky jako seznam
posledni_radka = radky[-1]
print("Poslední řádek tabulky:", posledni_radka)

# Vytvoření tabulky bez prvních dvou řádků
bez_prvnich_dvou_radku = radky[2:]
print("Tabulka bez prvních dvou řádků:")
for radka in bez_prvnich_dvou_radku:
    print(radka)

# Vytvoření tabulky pouze z prvních dvou řádků
prvni_dva_radky = radky[:2]
print("Tabulka pouze z prvních dvou řádků:")
for radka in prvni_dva_radky:
    print(radka)

# Vytvoření tabulky obsahující jen řádky 5, 6, 7, 8
radky_5678 = radky[4:8]
print("Tabulka obsahující řádky 5, 6, 7, 8:")
for radka in radky_5678:
    print(radka)

# Seřazení seznamu teplot vzestupně podle velikosti
sestupne_serazene_teploty = sorted(sloupce[1])
print("Seřazené teploty vzestupně:", sestupne_serazene_teploty)
