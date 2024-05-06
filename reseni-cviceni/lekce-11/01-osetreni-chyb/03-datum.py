from datetime import datetime

# Získání data narození od uživatele
datum_narozeni_input = input("Zadej datum ve formátu RRRR-MM-DD: ")

# Kontrola správnosti formátu
try:
    rok, mesic, den = datum_narozeni_input.split("-")
    # Převod na int pro zajištění, že jsou všechny části číselné
    rok, mesic, den = int(rok), int(mesic), int(den)

    # Využití datetime pro validaci správnosti data
    datum_narozeni = datetime.fromisoformat(datum_narozeni_input)
    print("Zadané datum narození je validní:", datum_narozeni)

except ValueError as e:
    print("Chyba při zadávání data:", e)

# except Exception as e:
#     print("Neočekávaná chyba:", e)
