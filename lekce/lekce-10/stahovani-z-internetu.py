# Tyto příkazy píšeme do terminálu!!!

# pip3 install requests
# pip install requests
# python - m pip install requests

import requests  # Import knihovny 'requests' pro práci s HTTP požadavky

# Zaslání GET požadavku na URL, které obsahuje JSON data o lidech
response = requests.get('https://api.kodim.cz/python-data/people')
# Převedení odpovědi z JSON formátu do Python slovníku
data = response.json()

# Výpis klíčů prvního prvku v seznamu dat, což obvykle ukazuje dostupné atributy dat
print(data[0].keys())
# Výpis celého prvního prvku seznamu, který obsahuje detailní informace o jedné osobě
print(data[0])

# Iterace přes seznam dat a výpis křestního jména a příjmení každé osoby
for i in data:
    print(i["first_name"], i["last_name"])
