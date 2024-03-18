def month_of_birth(rodne_cislo):
    # Zjistíme číslo měsíce podle rodného čísla
    mesic = int(rodne_cislo[2:4])
    
    # Pokud je číslo měsíce větší než 12, jedná se o ženu
    # a od čísla měsíce odečteme 50
    if mesic > 12:
        mesic -= 50
    
    return mesic

# Testování funkce
rodne_cislo1 = "9207054439"
rodne_cislo2 = "9555125899"

print("Měsíc narození z rodného čísla", rodne_cislo1, "je:", month_of_birth(rodne_cislo1))
print("Měsíc narození z rodného čísla", rodne_cislo2, "je:", month_of_birth(rodne_cislo2))
