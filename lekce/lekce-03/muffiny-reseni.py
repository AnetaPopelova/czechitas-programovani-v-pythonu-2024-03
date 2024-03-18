# Definice funkce 'vyrob_muffiny', která přijímá dva argumenty:
# 'pocet_muffinu' určuje, kolik muffinů se má vyrobit,
# a 'specialni_ingredience', což je seznam speciálních ingrediencí, s výchozí hodnotou prázdného seznamu.
def vyrob_muffiny(pocet_muffinu, specialni_ingredience=[]):
    # Vypíše, kolik muffinů se bude vyrábět.
    print(f"Vyrábím {pocet_muffinu} muffinů.")
    # Kontroluje, zda byly poskytnuty nějaké speciální ingredience.
    if specialni_ingredience:
        # Pokud ano, vypíše, které speciální ingredience se přidávají.
        print(f"Přidávám speciální ingredience: {specialni_ingredience}")
    else:
        # Pokud ne, informuje, že se vyrábějí muffiny bez speciálních ingrediencí.
        print("Bez speciálních ingrediencí")
    # Funkce vrací počet vyrobených muffinů.
    return pocet_muffinu

# Volání funkce 'vyrob_muffiny' s argumenty 40 a seznamem obsahujícím 'čokoláda',
# což znamená, že se má vyrobit 40 muffinů s čokoládou.
pocet = vyrob_muffiny(40, ["čokoláda"])
# Vypíše celkový počet vyrobených muffinů.
print(f"Celkově vyrobeno: {pocet} muffinů.")

# Příklad v komentáři ukazuje alternativní volání funkce, kde se vyrábí 5 muffinů
# s přidáním speciálních ingrediencí čokoláda a vanilka.
# Výstup by pak byl:
# Vyrábím 5 muffinů.
# Přidávám speciální ingredience: ['čokoláda', 'vanilka']
# Celkově vyrobeno: 5 muffinů.
pocet = vyrob_muffiny(5, ["čokoláda", "vanilka"])
print(f"Celkově vyrobeno: {pocet} muffinů.")
