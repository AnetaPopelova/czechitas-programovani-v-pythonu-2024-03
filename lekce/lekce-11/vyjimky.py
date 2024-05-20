# Zadat věk uživatele
vek = input("Zadej vek:")
# Porovnání věku, jestli je větší než 15 (chyba: input vrací string, ne int)
if vek > 15:  # TypeError
    print("Vitej!")

# Druhé zadání věku uživatele
vek = input("Zadej vek:")  # input = deset
# Porovnání věku, jestli je větší než 15 (chyba: input vrací string, ne int)
if vek > 15:  # TypeError
    print("Vitej!")

# Chybí odsazení v bloku if
if True:
print("Tohle bude chyba")  # IndentationError

# Proměnná není definována
print(promenna)  # NameError

# Nesprávná operace: sčítání řetězce a čísla
print("Ahoj" + 5)  # TypeError

# Nesprávný převod řetězce na celé číslo
print(int("abc"))  # ValueError

# Přístup k neexistujícímu indexu v seznamu
seznam = [5, 4, 8]
print(seznam[20])  # IndexError

# Dělení nulou
print(10 / 0)  # ZeroDivisionError

# Otevření neexistujícího souboru
open("neexistujici_soubor.txt")  # FileNotFoundError

# Funkce pro kontrolu, jestli je číslo liché


def is_odd(number):
    return number % 2 == 0  # Chyba: funkce vrací True pro sudá čísla, ne lichá


# Testování funkce s chybným očekáváním
assert is_odd(5) == True  # AssertionError
print(is_odd(5))

# Zadání věku uživatele
vek = input("Zadej vek: ")
# Kontrola, jestli je vstup číslo
if not vek.isdigit():
    print("Musis tam dat cislo")
    exit()

# Převod věku na celé číslo
vek = int(vek)
# Porovnání věku, jestli je větší než 15
if vek > 15:
    print("Vitej")
else:
    print("Nemas tu co delat")

# Nekonečný cyklus pro opakované zadávání věku
while True:
    try:
        # Zadání věku uživatele
        vek = input("Zadej vek:")
        # Převod věku na celé číslo
        vek = int(vek)
        # Porovnání věku, jestli je větší než 15
        if vek > 15:
            print("Vitej")
            break  # Ukončení cyklu
        else:
            print("Nemas tu co delat")
            break  # Ukončení cyklu
    except ValueError:
        # Zpracování chyby při neplatném vstupu
        print("Je treba zadat cislo. ")
