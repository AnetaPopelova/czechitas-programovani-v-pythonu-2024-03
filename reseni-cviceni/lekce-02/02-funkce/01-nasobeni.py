# Napiš funkci mult, která bude mít dva číselné parametry. 
# Funkce oba parametry vynásobí a vrátí výsledek.

def mult(a, b):
    """
    Vynásobí oba parametry a vrátí výsledek.

    Args:
        a (int or float): První číslo.
        b (int or float): Druhé číslo.

    Returns:
        int or float: Výsledek násobení.
    """
    return a * b

# Příklad použití funkce
cislo1 = 5
cislo2 = 7
vysledek = mult(cislo1, cislo2)
print(f"Výsledek násobení {cislo1} a {cislo2} je {vysledek}.")
