# Import modulu pro logování, který umožní zaznamenávat chyby a další důležité informace
import logging

# Nastavení logování
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def preved_na_float(cislo):
    """
    Převede řetězec na desetinné číslo, kontroluje správnost formátu a řeší chyby.

    :param cislo: Řetězec reprezentující desetinné číslo.
    :return: Desetinné číslo nebo None, pokud dojde k chybě.
    """
    try:
        return float(cislo)
    except ValueError:
        logging.error(f"Chyba při konverzi: '{cislo}' není platné číslo.")
        return None

def zpracuj_soubor(cesta_k_souboru):
    """
    Čte řádky ze souboru, zpracovává a sumuje kilometráž.

    :param cesta_k_souboru: Cesta k textovému souboru s údaji o kilometrech.
    :return: Celkový počet kilometrů jako float.
    """
    celkovy_pocet_km = 0
    with open(cesta_k_souboru, 'r', encoding='utf-8') as soubor:
        for radek in soubor:
            radek = radek.replace(',', '.').strip()
            try:
                # Předpokládáme, že kilometráž je druhý údaj na každém řádku
                kilometry = radek.split()[1]
            except IndexError:
                logging.error(f"Řádek '{radek}' nemá očekávaný formát.")
                continue

            km = preved_na_float(kilometry)
            if km is not None:
                celkovy_pocet_km += km

    return celkovy_pocet_km

# Cesta k souboru, který obsahuje data
cesta = 'reseni-cviceni/lekce-09/01-cteni-souboru/auta.txt'

# Zpracování souboru a výpis výsledku
total_km = zpracuj_soubor(cesta)
print(f"Celkový počet kilometrů: {total_km} km")  # Převod z tisíc kilometrů na kilometry již není nutný
