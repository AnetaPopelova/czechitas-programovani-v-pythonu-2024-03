# Seznam čísel
cisla = [5, 3, 8, 1, 9, 2, 7]

# Inicializace proměnné pro uchování největšího prvku
nejvetsi_prvek = cisla[0]

# Projdi všechna čísla v seznamu a porovnej je s největším nalezeným prvkem
for cislo in cisla:
    if cislo > nejvetsi_prvek:
        nejvetsi_prvek = cislo

# Vypsání největšího prvku
print("Největší prvek je:", nejvetsi_prvek)

