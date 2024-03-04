# Tento kód pracuje se seznamy v Pythonu. 

# Definice seznamu jmen
seznam = ['Lenka', 'Jana', 'Martina', 'Zuzka']

# Přidání nového jména do seznamu
seznam.append('Katerina')

# Výpis upraveného seznamu a jeho délky
print(seznam)
print(len(seznam)) # Výpis počtu prvků v seznamu

# Definice seznamu seznamů s původním seznamem a novým seznamem jmen
vsechny_seznamy = [seznam, ['Jakub', 'Filip']]
# Různé způsoby výpisu prvků a podseznamů
print(vsechny_seznamy)
print((vsechny_seznamy))
print((vsechny_seznamy[0]))
print((vsechny_seznamy[0][0]))
print((vsechny_seznamy[0][0][0])) 
print((vsechny_seznamy[0][0]), vsechny_seznamy[1][0]) # Výpis prvního jména v prvního seznamu a prvního jména v druhém seznamu


# Iterace přes seznam čísel a přičtení 1 k každému číslu
cisla = [1, 5, 4, 1, 1]
for i in cisla:
    print(i + 1)

# Dvojitá iterace: první iterace přes seznam seznamů, druhá iterace přes jednotlivá jména v těchto seznamech
for i in vsechny_seznamy:
    for jmeno in i:
        print(jmeno)
