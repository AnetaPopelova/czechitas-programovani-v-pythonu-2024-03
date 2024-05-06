# Zeptáme se uživatele na první číslo
num1 = float(input("Zadej první číslo: "))

# Zeptáme se uživatele na druhé číslo
num2 = float(input("Zadej druhé číslo: "))


try:
    # Výpočet a vypsání výsledku dělení
    vysledek = num1 / num2
    print("Výsledek dělení je:", vysledek)
except ZeroDivisionError:
    # Ošetření dělení nulou
    print("Dělení nulou není povoleno.")
