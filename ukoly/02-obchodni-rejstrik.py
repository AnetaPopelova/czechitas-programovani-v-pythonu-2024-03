import requests
import json

# Část 1: Získání informací o subjektu podle IČO
ico = input("Zadejte IČO subjektu: ")

# Sestavení URL pro GET request
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

# Odeslání GET requestu
response = requests.get(url)
data = response.json()

# Získání požadovaných dat
business_name = data.get('obchodniJmeno')
address = data.get('textovaAdresa')

# Výpis informací
print(business_name)
print(address)


# Část 2: Vyhledávání subjektů podle názvu
# Vstup od uživatele pro hledaný název subjektu
search_name = input("Zadejte název subjektu pro vyhledání: ")

# Definice hlavičky a dat pro POST request
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = json.dumps({"obchodniJmeno": search_name})

# Odeslání POST requestu
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
response = requests.post(url, headers=headers, data=data)
response_data = response.json()

# Získání a výpis počtu a detailů nalezených subjektů
total_found = response_data.get('pocetCelkem')
print(f"Nalezeno subjektů: {total_found}")
for subjekt in response_data.get('ekonomickeSubjekty', []):
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")

# # Bonus: Integrace právní formy do výstupu
# # Funkce pro hledání právní formy
# def find_legal_form(code, legal_forms):
#     for item in legal_forms:
#         if item['kod'] == code:
#             return item['nazev']
#     return "Neznámá právní forma"

# # Získání číselníku právních forem
# headers = {
#     "accept": "application/json",
#     "Content-Type": "application/json",
# }
# data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
# legal_forms_url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
# legal_response = requests.post(legal_forms_url, headers=headers, data=data)
# legal_data = legal_response.json()
# legal_forms = legal_data['ciselniky'][0]['polozkyCiselniku']

# # Přidání právní formy do výpisu subjektů
# print(f"Nalezeno subjektů: {total_found}")
# for subjekt in response_data.get('ekonomickeSubjekty', []):
#     legal_form_name = find_legal_form(subjekt['pravniForma']['kod'], legal_forms)
#     print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}, {legal_form_name}")
