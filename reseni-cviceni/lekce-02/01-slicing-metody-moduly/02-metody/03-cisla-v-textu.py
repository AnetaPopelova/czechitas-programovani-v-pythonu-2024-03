hodnoty = '12.1 1.68 7.45 -11.51'

# Rozdělení řetězce na seznam čísel
seznam_cisel = hodnoty.split()

# Převedení posledního čísla na float, přičtení 0.25 a převedení zpět na řetězec
posledni_cislo = float(seznam_cisel[-1]) + 0.25
seznam_cisel[-1] = str(posledni_cislo)

# Spojení upraveného seznamu zpět do řetězce
upraveny_retezec = ' '.join(seznam_cisel)

print(upraveny_retezec)
