import json

# Načtení dat ze souboru
with open("lekce/lekce-10/zavod.json", "r") as file:
    data = json.load(file)


finishers = []

# Projdi seznam závodníků
for zavodnik in data:
    if zavodnik["casy"]["oficialni"] != "DNF":
        # Přidej jméno a čas do seznamu finishers, pokud závodník dokončil závod
        finishers.append([zavodnik["jmeno"], zavodnik["casy"]["oficialni"]])

print(finishers[1])
