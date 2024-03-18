import random

def roulette(cislo_rady, sazka):
    # Vygenerování náhodného čísla od 0 do 36
    cislo_rulety = random.randint(0, 36)
    
    # Určení, do které řady číslo náleží
    if cislo_rulety == 0:  # Pokud padne 0, uživatel vždy prohrává
        return 0
    elif cislo_rulety % 3 == 1:
        rada_rulety = 1
    elif cislo_rulety % 3 == 2:
        rada_rulety = 2
    else:
        rada_rulety = 3
    
    # Porovnání sázky uživatele s řadou rulety
    if cislo_rady == rada_rulety:
        return 2 * sazka  # Uživatel vyhrává dvojnásobek sázky
    else:
        return 0  # Sázka propadá

# Zeptat se uživatele na číslo řady a výši sázky
cislo_rady = int(input("Na kterou z řad sázíte? (1, 2 nebo 3): "))
sazka = float(input("Jakou částku vsadíte? "))

# Zavolat funkci roulette s parametry zadanými uživatelem
vyhra = roulette(cislo_rady, sazka)

# Výpis výsledku sázky
if vyhra > 0:
    print("Gratulujeme, vyhráli jste!", vyhra)
else:
    print("Bohužel jste prohráli. Vaše sázka propadá.")
