def obalit_hvezdickami(retezec, znak='*'):
    delka = len(retezec) + 4
    oddelovac = znak * delka
    obsah = f"{znak} {retezec} {znak}"
    print(oddelovac)
    print(obsah)
    print(oddelovac)

# Testování funkce
slovo = input("Zadej slovo: ")
obalit_hvezdickami(slovo)