import requests
import json

# URL API
url = "https://api.kodim.cz/python-data/people"

# Stáhnout data z API
response = requests.get(url)
data = response.json()  # převedení JSON dat na Python slovníky

# Zjistit celkový počet lidí
total_people = len(data)
print("Celkový počet lidí:", total_people)

# Zjistit, jaké všechny informace máme o jednotlivých osobách
if total_people > 0:
    print("Informace dostupné o osobách:", list(data[0].keys()))

# Zjistit počet mužů a žen
male_count = sum(1 for person in data if person["gender"] == "Male")
female_count = sum(1 for person in data if person["gender"] == "Female")
print("Počet mužů:", male_count)
print("Počet žen:", female_count)
