import math

# Vstup od uživatele
cislo = float(input("Zadejte desetinné číslo: "))

# Zaokrouhlení nahoru
zaokrouhleni_nahoru = math.ceil(cislo)

# Zaokrouhlení dolů
zaokrouhleni_dolu = math.floor(cislo)

# Běžné Pythonovské zaokrouhlení
zaokrouhleni_python = round(cislo)

# Výstup
print("Zaokrouhlení nahoru:", zaokrouhleni_nahoru)
print("Zaokrouhlení dolů:", zaokrouhleni_dolu)
print("Běžné zaokrouhlení:", zaokrouhleni_python)
