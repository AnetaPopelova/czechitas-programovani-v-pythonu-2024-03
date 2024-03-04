# Tento kód provádí několik základních operací s proměnnými a demonstruje práci s různými datovými typy v Pythonu.

# Deklarace proměnné 'cislo' s hodnotou 1 (celé číslo)
cislo = 1
# Deklarace proměnné 'text' s hodnotou 'dva' (řetězec)
text = 'dva'
# Deklarace proměnné 'boolean' s hodnotou True (logická hodnota)
boolean = True
# Deklarace seznamu 'seznam' obsahujícího čtyři celá čísla
seznam  = [1, 5, 99, 8]
# Deklarace proměnné 'desetinne_cislo' s hodnotou 1.1 (desetinné číslo)
desetinne_cislo = 1.1

# Výpis typu proměnné 'cislo' (int)
print(type(cislo))
# Změna typu proměnné 'cislo' na float a následný výpis nového typu
cislo = float(cislo)
print(type(cislo))

# Příklady zakomentovaných převodů mezi datovými typy
# str() # Převod na řetězec
# int() # Převod na celé číslo
# float() # Převod na desetinné číslo

# Načtení uživatelského vstupu a uložení do proměnné 'uzivatelova_promenna'
uzivatelova_promenna = input("Zapis ciselnou hodnotu:")
# Převod uživatelského vstupu na celé číslo
uzivatelova_promenna = int(uzivatelova_promenna)
# Alternativní způsob načtení celého čísla od uživatele (zakomentovaný)

# Výpis desetinásobku hodnoty uživatelské proměnné
print(uzivatelova_promenna * 10)
# Formátovaný výpis desetinásobku hodnoty s popisem
print(f"zadana hodnota je {uzivatelova_promenna * 10}")
