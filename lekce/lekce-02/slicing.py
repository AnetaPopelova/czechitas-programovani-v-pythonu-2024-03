# Inicializace seznamu s názvem venecky
venecky = [1, 2, 4, 1, 6, 0, 1]

# Výpis prvního prvku seznamu
print(venecky[0])

# Změna prvního prvku seznamu na 3
venecky[0] = 3
# Výpis upraveného seznamu
print(venecky)

# Výpis prvních pěti prvků seznamu
print(venecky[0:5])
# Stejně jako výše, ale používá zkrácený zápis
print(venecky[:5])
# Výpis prvků seznamu od šestého prvku do konce
print(venecky[5:])
# Výpis každého druhého prvku seznamu
print(venecky[::2])
# Výpis každého druhého prvku od druhého do pátého prvku
print(venecky[1:5:2])
# Konkatenace (spojení) prvních pěti prvků s každým druhým prvkem od šestého dále
print(venecky[0:5] + venecky[5::2])

# Výpis délky seznamu
print(len(venecky))
# Výpis součtu prvků v seznamu
print(sum(venecky))
# Výpis nejmenšího prvku v seznamu
print(min(venecky))
# Výpis největšího prvku v seznamu
print(max(venecky))
# Výpis seznamu seřazeného od nejmenšího po největší prvek
print(sorted(venecky))

# Inicializace řetězce
retezec = "Mate radsi more, nebo hory?"
# Výpis délky řetězce
print(len(retezec))
# Výpis znaku s nejnižší hodnotou (komentář, protože sum není pro řetězce)
# print(sum(retezec))
# Výpis znaku s nejnižší hodnotou v ASCII tabulce v řetězci
print(min(retezec))
# Výpis znaku s nejvyšší hodnotou v ASCII tabulce v řetězci
print(max(retezec))
# Výpis řetězce seřazeného podle ASCII hodnot znaků, ale v opačném pořadí
print(sorted(retezec, reverse=True))

# Inicializace řetězce pro podmínkové příkazy
inzerat = "Na pracovni pozici se pouziva R."
# Podmínka zkontroluje, zda řetězec obsahuje "Python"
if "Python" in inzerat:
    # Tato větev se neprovede, protože "Python" v inzerátu není
    print("Beru to!")
# Podmínka zkontroluje, zda řetězec neobsahuje "Python"
if "Python" not in inzerat:
    # Tato větev se provede, protože "Python" v inzerátu není
    print("Neberu to!")
