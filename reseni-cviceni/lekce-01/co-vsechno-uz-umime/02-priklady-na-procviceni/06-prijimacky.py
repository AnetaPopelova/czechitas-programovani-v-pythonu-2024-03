school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

# Součet známek
sum_of_marks = 0

# Počet předmětů zahrnutých do průměru
count_of_subjects = 0

# Seznam předmětů, které se zahrnou do průměru
subjects = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]

# Projdi všechny položky ve vysvědčení
for subject, mark in school_report:
    # Pokud je předmět v seznamu jazyků, matematiky a fyziky, přičti známku k součtu
    if subject in subjects:
        sum_of_marks += mark
        count_of_subjects += 1

# Spočti průměr
average = sum_of_marks / count_of_subjects

# Vypiš průměr
print(f"Průměrná známka studenta/studentky ze základních předmětů je {average}.")
