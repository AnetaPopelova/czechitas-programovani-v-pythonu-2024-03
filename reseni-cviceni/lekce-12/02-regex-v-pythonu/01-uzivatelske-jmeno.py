import re

regularni_vyraz = re.compile(r"[a-z]{1,8}")

# uzivatelske_jmeno = input("Zadej uživatelského jména: ")
uzivatelske_jmeno = "ElonMusk"
vysledek = regularni_vyraz.fullmatch(uzivatelske_jmeno)

if vysledek:
    print("Uživatelské jméno je v pořádku.")
else:
    print("Uživatelské jméno nesplňuje požadavky")
