import re

kod = """
sender_field_title = "Příjemce"
copy_field_title = "Kopie"
if blind_copy:
    blind_copy_title = "Skrytá kopie"
if action == "send":
    button_title = "Odeslat"
else:
    button_title = "Uložit koncept"
"""

regularni_vyraz = re.compile(r"[\w_]* \= \"[\w ]*\"")
vysledky = regularni_vyraz.findall(kod)

for vysledek in vysledky:
    regularni_vyraz_vnitrni = re.compile(r"\"[\w ]*\"")
    vysledky_vnitrni = regularni_vyraz_vnitrni.findall(vysledek)
    print(vysledky_vnitrni[0])
