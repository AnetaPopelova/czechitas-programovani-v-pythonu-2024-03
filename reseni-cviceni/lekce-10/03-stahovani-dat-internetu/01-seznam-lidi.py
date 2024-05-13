import requests

# URL API
url = "https://api.kodim.cz/python-data/people"

# Stáhnout data z API
response = requests.get(url)
data = response.json()  # převedení JSON dat na Python slovníky

# Zjistit celkový počet lidí
total_people = len(data)
print("Celkový počet lidí:", total_people)


print("Informace dostupné o osobách:", list(data[0].keys()))

count_male = 0
count_female = 0
for i in data:
    if i["gender"] == "Male":
        count_male += 1
    elif i["gender"] == "Female":
        count_female += 1

print("Počet mužů:", count_male)
print("Počet žen:", count_female)
