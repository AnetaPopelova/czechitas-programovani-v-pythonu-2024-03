import requests


def get_name_day(day, month):
    # Zformátování datumu
    date = f"{day:02d}{month:02d}"

    # Příprava parametrů pro GET požadavek
    params = {"date": date}

    # API endpoint
    url = "https://svatky.adresa.info/json"

    # Odeslání požadavku
    response = requests.get(url, params=params)

    data = response.json()
    name = data[0]["name"]
    print(f"Svátek má: {name}")


# Spuštění funkce pro konkrétní datum
# Například pro zjištění, kdo má svátek 29. února
get_name_day(29, 2)
