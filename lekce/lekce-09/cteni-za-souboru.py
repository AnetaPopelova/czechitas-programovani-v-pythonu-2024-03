# Otevření souboru 'mereni.txt' v adresáři 'lekce/lekce-09' pro čtení s explicitním nastavením kódování na 'utf-8'
with open("lekce/lekce-09/mereni.txt", encoding="utf-8") as file:
    # Načtení celého obsahu souboru do proměnné 'text'
    text = file.read()
# Vypsání obsahu proměnné 'text' (obsahu souboru)
print(text)

# Inicializace prázdného seznamu pro uložení řádků souboru
lines = []
# Otevření souboru pro čtení s kódováním 'utf-8'
with open("lekce/lekce-09/mereni.txt", encoding="utf-8") as file:
    # Pro každý řádek v souboru
    for line in file:
        # Přidání řádku do seznamu 'lines'
        lines.append(line)
# Vypsání seznamu 'lines', který obsahuje jednotlivé řádky souboru
print(lines)

# Otevření souboru a načtení všech řádků pomocí metody readlines()
with open("lekce/lekce-09/mereni.txt", encoding="utf-8") as file:
    text = file.readlines()
# Vypsání seznamu 'text', který obsahuje řádky souboru
print(text)

# Inicializace seznamu pro uložení zpracovaných dat
output = []
# Otevření souboru pro čtení
with open("lekce/lekce-09/mereni.txt", encoding="utf-8") as file:
    # Pro každý řádek v souboru
    for line in file:
        # Rozdělení řádku na den a teplotu pomocí tabulátoru
        day, temp = line.split('\t')
        # Přidání dne a teploty převedené na typ float do seznamu 'output'
        output.append([day, float(temp)])
# Vypsání seznamu 'output', který obsahuje zpracované dvojice den a teplota
print(output)
