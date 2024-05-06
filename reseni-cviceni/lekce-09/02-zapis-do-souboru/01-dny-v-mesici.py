# Seznam obsahující počet dní v jednotlivých měsících roku
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Otevření souboru pro zápis
with open('kalendar.txt', 'w', encoding='utf-8') as soubor:
    # Iterace přes seznam pocty_dni
    for pocet in pocty_dni:
        # Zápis každého počtu dní na nový řádek v souboru
        soubor.write(f"{pocet}\n")

print("Seznam dní byl úspěšně zapsán do souboru 'kalendar.txt'.")
