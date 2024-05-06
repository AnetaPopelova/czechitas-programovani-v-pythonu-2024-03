# Otevření souboru a načtení řádků
celkovy_pocet_km = 0
with open('reseni-cviceni/lekce-09/01-cteni-souboru/auta.txt', 'r', encoding='utf-8') as soubor:
    for radek in soubor:
        # Odstranění přebytečných bílých znaků
        radek = radek.replace(',', '.').strip()
        kilometry = radek.split()[1]
        celkovy_pocet_km += float(kilometry)
        
# Výpis celkového součtu kilometrů
print(f"Celkový počet kilometrů: {celkovy_pocet_km * 1000} km")  # Převod z tisíc kilometrů na kilometry
