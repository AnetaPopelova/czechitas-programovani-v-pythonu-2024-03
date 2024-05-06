# Otevření souboru a načtení dat
with open('reseni-cviceni/lekce-09/03-cteni-na-doma/pasazeri.txt', 'r') as file:
    data = file.readlines()

# Funkce pro zpracování jedné řádky
def process_line(line):
    pairs = line.strip().split()  # Rozdělení řádku na jednotlivé páry
    tam = sum([int(pair.split(',')[0]) for pair in pairs])  # Součet prvních čísel v párech
    zpet = sum([int(pair.split(',')[1]) for pair in pairs])  # Součet druhých čísel v párech
    return tam, zpet

# Zpracování prvního dne
tam_first_day, zpet_first_day = process_line(data[0])

# Zpracování celého týdne
total_tam_week, total_zpet_week = 0, 0
for line in data:
    tam, zpet = process_line(line)
    total_tam_week += tam
    total_zpet_week += zpet

# Výpis výsledků
print("První den:")
print(f"Celkem jelo směrem tam {tam_first_day} pasažérů.")
print(f"Celkem jelo směrem zpět {zpet_first_day} pasažérů.")
print("\nCelý týden:")
print(f"Celkem jelo směrem tam {total_tam_week} pasažérů.")
print(f"Celkem jelo směrem zpět {total_zpet_week} pasažérů.")
