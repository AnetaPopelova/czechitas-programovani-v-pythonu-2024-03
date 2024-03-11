hodnoty = ['12', '1', '7', '-11']

# Uložení hodnoty na třetí pozici do proměnné
hodnota_na_treti_pozici = hodnoty[2]

# Přičtení 4 k hodnotě a uložení výsledku do proměnné
vysledek = int(hodnota_na_treti_pozici) + 4

# Převedení výsledku zpět na řetězec a uložení na třetí pozici v seznamu hodnoty
hodnoty[2] = str(vysledek)

print(hodnoty)
