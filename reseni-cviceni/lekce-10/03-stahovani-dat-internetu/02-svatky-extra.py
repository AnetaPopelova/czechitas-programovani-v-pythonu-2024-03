import requests
import json


def get_name_day(day, month):
    # Zformátování datumu
    date = f"{day:02d}{month:02d}"

    # Příprava parametrů pro GET požadavek
    params = {"date": date}

    # API endpoint
    url = "https://svatky.adresa.info/json"

    try:
        # Odeslání požadavku s využitím kontextového manažera
        with requests.get(url, params=params) as response:
            # Kontrola, zda požadavek proběhl úspěšně
            response.raise_for_status()  # Vyvolá výjimku, pokud je stavový kód mimo 200-299
            data = response.json()
            if data:
                name = ", ".join(
                    item["name"] for item in data
                )  # Zpracování případu více jmen
                print(f"Svátek má: {name}")
            else:
                print("V tento den nemá svátek nikdo.")
    except requests.RequestException as e:
        print(f"Chyba při získávání dat: {e}")
    except json.JSONDecodeError:
        print("Nepodařilo se dekódovat JSON data.")
    except IndexError:
        print("Data neobsahují očekávanou strukturu.")


# Spuštění funkce pro konkrétní datum
# Například pro zjištění, kdo má svátek 29. února
get_name_day(29, 2)
