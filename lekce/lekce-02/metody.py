# Inicializace řetězce s hodnotou 'Python'
retezec = 'Python'

# Tento řádek je zakomentovaný a pokud by byl odkomentován, vyhodil by chybu, protože správná syntaxe je retezec.upper(), ne upper(retezec)
# print(upper(retezec))

# Výpis řetězce převedeného na velká písmena
print(retezec.upper())
# Výpis řetězce převedeného na malá písmena
print(retezec.lower())

# Re-inicializace řetězce s mezerami na začátku a na konci
retezec = '   Python    '
# Výpis řetězce včetně mezer
print(retezec)
# Výpis řetězce s odstraněnými mezerami na začátku a na konci
print(retezec.strip())

# Rozdělení řetězce na seznam podřetězců dle mezery
print('aa bb cc dd ee'.split(' '))
# Rozdělení řetězce na seznam podřetězců dle tečky
print('aa.bb.cc.dd.ee'.split('.'))

# Inicializace seznamu s řetězci reprezentujícími čísla
retezec = ['1', '2', '3', '4']
# Spojení prvků seznamu do jednoho řetězce s vloženými plusy mezi nimi
print('+'.join(retezec))

# Tento řádek je zakomentovaný a pokud by byl odkomentován, vyhodil by chybu, protože metoda join() se musí volat na řetězci, který slouží jako spojovník, a v argumentu dostane seznam
# print(retezec.join('+'))

# Inicializace řetězce inzerátu
inzerat = "Na pracovni pozici se pouziva R."
# Výpis inzerátu, kde je 'R' nahrazeno 'Python'
print(inzerat.replace('R', 'Python'))
