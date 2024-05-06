import re

regularni_vyraz = re.compile(
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}"
)

"""
2[0-9]{2} odpovídá číslům od 200 do 255.
1[0-9]{2} odpovídá číslům od 100 do 155.
[1-9]?[0-9] odpovídá číslům od 0 do 55.
Výraz celkem hledá čtveřici takových čísel, oddělených tečkami.
"""

# adresa_severu = input("Zadej adresu serveru: ")
adresa_severu = "192.168.1.0"  # "325.125.100.128"

vysledek = regularni_vyraz.fullmatch(adresa_severu)
if vysledek:
    print("Odesílám zprávu.")
else:
    print("Adresa není platná.")
