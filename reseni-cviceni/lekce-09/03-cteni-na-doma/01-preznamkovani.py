# Přečtení a konverze známek pomocí obyčejného for cyklu
with open('reseni-cviceni/lekce-09/03-cteni-na-doma/znamky-za-semestr.txt', 'r', encoding='utf-8') as infile, open('reseni-cviceni/lekce-09/03-cteni-na-doma/znamky-za-semestr_nove.txt', 'w', encoding='utf-8') as outfile:
    grades = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'F'}
    for line in infile:
        parts = line.strip().split('\t')
        # Inicializace seznamu pro konvertované známky
        converted = [parts[0], parts[1]]  # Přidání jmen do seznamu
        # Procházení známek a jejich konverze
        for mark in parts[2:]:
            if mark in grades:
                converted.append(grades[mark])  # Přidání převedené známky do seznamu
            else:
                converted.append(mark)  # Přidání nezměněné známky
        # Zápis konvertovaných dat do výstupního souboru
        outfile.write('\t'.join(converted) + '\n')
