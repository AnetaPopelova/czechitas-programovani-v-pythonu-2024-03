# Seznam hostů a jejich hesel
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

# Získání jména hosta od uživatele
jmeno_hosta = input("Zadej jméno hosta: ")

# Kontrola, zda je host na seznamu
if jmeno_hosta in passwords:
    # Získání hesla od uživatele
    zadane_heslo = input("Zadej heslo: ")
    # Kontrola, zda zadané heslo odpovídá heslu v seznamu
    if zadane_heslo == passwords[jmeno_hosta]:
        print("Smíš vstoupit.")
    else:
        print("Nesprávné heslo.")
else:
    print("Host není na seznamu.")
