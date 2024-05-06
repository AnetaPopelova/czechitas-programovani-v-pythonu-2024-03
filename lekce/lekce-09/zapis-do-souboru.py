# Text, který chceme zapsat do souboru
text = "Chci tento text zapsat do souboru."

# Otevření souboru "soubor.txt" v režimu přidání (mode="a") s UTF-8 kódováním
with open("soubor.txt", mode="a", encoding="utf-8") as output_file:
    # Vytiskne text do souboru pomocí funkce print, přičemž specifikuje, že výstupním souborem je output_file
    print(text, file=output_file)

# Seznam jmen
names = ['Zuzana', 'Olga', 'Martina']

# Otevření souboru "ucastnictvo.txt" ve složce "lekce/lekce-09" v režimu zápisu (mode='w') s UTF-8 kódováním
with open('lekce/lekce-09/ucastnictvo.txt', mode='w', encoding='utf-8') as output_file:
    # Iterace přes jména v seznamu
    for name in names:
        # Vytiskne každé jméno do souboru pomocí funkce print, opět specifikuje output_file jako výstupní soubor
        print(name, file=output_file)
