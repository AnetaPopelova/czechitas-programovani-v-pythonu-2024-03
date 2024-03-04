# Žádost o zadání počtu vstupenek a převedení vstupu na celé číslo
pocet_vstupenek = int(input("Kolik chces vstupenek? "))
# Nastavení ceny jedné vstupenky
cena_vstupenky = 9

# Výpočet celkové ceny na základě počtu vstupenek a ceny za jednu vstupenku
celkova_cena = pocet_vstupenek * cena_vstupenky

# Podmínka pro aplikaci slevy, pokud celková cena přesáhne 500
if celkova_cena > 500:
    sleva = 0.1  # Procentuální hodnota slevy
    celkova_cena = celkova_cena * (1 - sleva)  # Aplikace slevy na celkovou cenu
# Podmínka pro případ, že celková cena je menší než 10
elif celkova_cena < 10:
    print("To nemyslis vazne, za tolik si nic nekoupis. ")
# Výzva k utracení více peněz pro získání slevy, pokud není splněna žádná z předchozích podmínek
else: 
    print("Utrat vic, dostanes slevu")

# Výpis výsledné celkové ceny po aplikaci slevy
print(celkova_cena)

