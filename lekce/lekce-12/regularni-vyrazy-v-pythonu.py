import re

# Vytvoření regulárního výrazu pro rodné číslo, které má 9 nebo 10 číslic
regex_rodne_cislo = re.compile(r"\d{9,10}")

# Vstupní řetězce obsahující rodná čísla
retezec = "Moje rodne cislo je 9511121234"
presna_shoda = "9511121234"
na_zacatku = "9511121234 je moje rodne cislo"

# Vyhledání rodného čísla kdekoliv v řetězci
print(regex_rodne_cislo.search(retezec))      # Najde první shodu v řetězci
print(regex_rodne_cislo.search(presna_shoda))  # Najde první shodu v řetězci
print(regex_rodne_cislo.search(na_zacatku))   # Najde první shodu v řetězci

# Vyhledání rodného čísla pouze na začátku řetězce
# Vrátí None, protože shoda není na začátku
print(regex_rodne_cislo.match(retezec))
# Najde shodu, protože je na začátku
print(regex_rodne_cislo.match(presna_shoda))
# Najde shodu, protože je na začátku
print(regex_rodne_cislo.match(na_zacatku))

# Kontrola, zda celý řetězec odpovídá rodnému číslu
# Vrátí None, protože celý řetězec neodpovídá
print(regex_rodne_cislo.fullmatch(retezec))
# Najde shodu, protože celý řetězec odpovídá
print(regex_rodne_cislo.fullmatch(presna_shoda))
# Vrátí None, protože celý řetězec neodpovídá
print(regex_rodne_cislo.fullmatch(na_zacatku))

# Nový regulární výraz pro rodné číslo
regex_rodne_cislo = re.compile(r"\d{9,10}")
moje_rodne_cislo = "1256789"

# Kontrola, zda můj řetězec odpovídá rodnému číslu
if regex_rodne_cislo.fullmatch(moje_rodne_cislo):
    print("OK")  # Tiskne "OK" pokud řetězec přesně odpovídá
else:
    print("NOK")  # Tiskne "NOK" pokud řetězec neodpovídá

# Víceřádkový řetězec s několika rodnými čísly
zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kotníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""

# Vyhledání všech rodných čísel v záznamu
print(regex_rodne_cislo.findall(zapis))  # Vrátí seznam všech shod

# Nahrazení všech rodných čísel v záznamu za "XXXXXXXXXX"
# Nahrazuje všechny shody řetězcem "XXXXXXXXXX"
print(regex_rodne_cislo.sub("X" * 10, zapis))
