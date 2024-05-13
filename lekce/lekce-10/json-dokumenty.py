import json

# Cesta k souboru s JSON daty o absolventech
path = "lekce/lekce-10/absolventi.json"

# Otevření souboru JSON a načtení jeho obsahu do proměnné 'absolvents'
with open(path, encoding="utf-8") as file:
    absolvents = json.load(file)

# Výpis všech dat o absolventech
print(absolvents)
# Iterace přes seznam absolventů a výpis jejich docházky
for i in absolvents:
    print(i["dochazka"])

# Zakomentovaný řádek funkce, která není definována nebo použita v ukázce kódu
# dump()

# Slovník reprezentující počet pracovních hodin za každý den v týdnu
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 10, 'pa': 4}
# Zápis slovníku 'hours' do JSON souboru
with open('lekce/lekce-10/hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file)

# Slovník s jednou položkou pro demonstraci zápisu s diakritikou
data = {"řeřicha": "Česká Třebová"}
# Zápis dat do JSON souboru s nastavením pro zachování diakritiky
with open("lekce/lekce-10/rericha.json", mode="w", encoding="utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False)

# Načtení dat o běžcích ze souboru JSON
with open("lekce/lekce-10/zavod.json", encoding="utf-8") as file:
    runners = json.load(file)
# Výpis prvního běžce v seznamu
print(runners[0])
# Výpis jména prvního běžce
print(runners[0]["jmeno"])
