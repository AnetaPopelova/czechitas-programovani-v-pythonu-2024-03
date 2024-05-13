import requests

# Zformátování datumu
day = 29
month = 2
date = f"{day:02d}{month:02d}"


# Příprava parametrů pro GET požadavek
params = {"date": date}

# API endpoint
url = "https://svatky.adresa.info/json"

# Odeslání požadavku
response = requests.get(url, params=params)

# Zpracování odpovědi a extrakce jména
data = response.json()
name = data[0]["name"]

# Výpis jména osoby, která má na tento den svátek
print(f"Svátek má: {name}")
