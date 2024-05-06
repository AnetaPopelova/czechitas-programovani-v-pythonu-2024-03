import csv

# Příprava datové struktury
class_birthdays = {}

# Načtení dat z CSV souboru
with open("reseni-cviceni/lekce-10/kids.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        name, classroom, birthdate = row
        # získání měsíce z data narození
        month = int(birthdate.split(".")[1].strip())

        # Kontrola, zda třída již existuje v slovníku
        if classroom not in class_birthdays:
            class_birthdays[classroom] = {}

        # Kontrola, zda měsíc již existuje pro tuto třídu
        if month not in class_birthdays[classroom]:
            class_birthdays[classroom][month] = []

        # Přidání jména do příslušného seznamu
        class_birthdays[classroom][month].append(name)

# Vytvoření výstupních souborů pro každou třídu
for classroom in class_birthdays:
    with open(
        f"reseni-cviceni/lekce-10/{classroom}.txt", "w", encoding="utf-8"
    ) as file:
        file.write(f"Třída {classroom}\n")
        for month in sorted(class_birthdays[classroom].keys()):
            names = ", ".join(sorted(class_birthdays[classroom][month]))
            file.write(f"{month}: {names}\n")
