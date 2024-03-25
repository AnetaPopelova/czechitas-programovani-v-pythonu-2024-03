# Definice slovníku s informacemi o Velikonocích v roce 2024
velikonoce = {
    "datum": "1. dubna 2024",  # Datum Velikonoc v roce 2024
    "velikonocni_symboly": ["vajíčka", "zajíčci", "pomlázka", "jarní květiny"],  # Seznam velikonočních symbolů
    "pocasi": {
        "teplota": 15,  # Průměrná teplota v °C během Velikonoc
        "popis": "částečně oblačno"  # Popis počasí
    },
    "tradice": {
        "koledovani": True,  # Přítomnost tradice koledování
        "malovani_vajicek": True,  # Tradice malování vajíček
        "velikonocni_obed": ["beránek", "vejce", "nádivka", "kopřivy"]  # Složení velikonočního oběda
    }
}

# Získání a výpis data Velikonoc
datum_velikonoc = velikonoce["datum"]
print(f"Datum Velikonoc v roce 2024: {datum_velikonoc}")

# Získání a výpis velikonočních symbolů
velikonocni_symboly = velikonoce["velikonocni_symboly"]
print("Velikonoční symboly:", ", ".join(velikonocni_symboly))

# Získání a výpis průměrné teploty během Velikonoc
teplota = velikonoce["pocasi"]["teplota"]
print(f"Průměrná teplota během Velikonoc: {teplota}°C")

# Získání a výpis popisu počasí během Velikonoc
popis_pocasi = velikonoce["pocasi"]["popis"]
print(f"Počasí během Velikonoc: {popis_pocasi}")

# Získání a výpis informace o koledování
koledovani = velikonoce["tradice"]["koledovani"]
print(f"Koledování během Velikonoc: {'Ano' if koledovani else 'Ne'}")

# Získání a výpis složení velikonočního oběda
velikonocni_obed = velikonoce["tradice"]["velikonocni_obed"]
print("Jídla pro Velikonoční oběd:", ", ".join(velikonocni_obed))

# Aktualizace slovníku `velikonoce`
velikonoce["pocasi"].update({"srazky": "zadne"})
velikonoce["pocasi"]["tlak"] = "nizky"
print(velikonoce)  

# Přidání nového symbolu do seznamu velikonočních symbolů
velikonoce["velikonocni_symboly"].append("kuratko")
print(velikonoce)