# Vysvědčení ve formě slovníku
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# Spočítání průměrné známky
prumer = sum(school_report.values()) / len(school_report)
print("Průměrná známka:", prumer)

# Vypsání předmětů se známkou 1
print("Předměty se známkou 1:")
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)
