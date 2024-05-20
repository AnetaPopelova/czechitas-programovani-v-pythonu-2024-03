# Inicializace prázdného seznamu pro uložení jmen
names = []

# Definování cesty k souboru (momentálně špatná cesta, správná cesta je zakomentována)
file_path = "spatna_cesta.txt"
# file_path = "lekce/lekce-11/names.txt"

# Pokus o otevření souboru a načtení jeho obsahu
try:
    # Otevření souboru s kódováním UTF-8
    with open(file_path, encoding="utf-8") as file:
        # Načtení jednotlivých řádků souboru do seznamu names
        for line in file:
            names.append(line)
    # Vytištění načtených jmen
    print(names)
# Zpracování chyby, pokud soubor neexistuje
except FileNotFoundError as err:
    print(f"Soubor {file_path} neexistuje. {err}")
# Zpracování chyby, pokud nemáme přístupová práva k souboru
except PermissionError:
    print(f"K souboru {file_path} nemáš přístupová práva.")
# Zpracování jakýchkoliv jiných chyb
except Exception as err:
    print(f"Chyba při načítání souboru. {err}")
# Tento blok se provede, pokud nedojde k žádné výjimce
else:
    print("Super! Načteno!")
# Tento blok se provede vždy, bez ohledu na to, zda došlo k výjimce nebo ne
finally:
    print("TEST FINALLY")


while True:
    try:
        # Zadání věku uživatele
        vek = input("Zadej vek: ")
        # Převod věku na celé číslo
        vek = int(vek)
        # Zkontrolování, zda je věk menší než nula
        if vek < 0:
            raise ValueError("Věk nemůže být menší než nula.")
        # Porovnání věku, jestli je větší než 15
        if vek > 15:
            print("Vitej")
            break  # Ukončení cyklu
        else:
            print("Nemas tu co delat")
            break  # Ukončení cyklu
    except ValueError as e:
        # Zpracování chyby při neplatném vstupu nebo věku menším než nula
        print(f"Chyba: {e}. Je třeba zadat kladné číslo.")

