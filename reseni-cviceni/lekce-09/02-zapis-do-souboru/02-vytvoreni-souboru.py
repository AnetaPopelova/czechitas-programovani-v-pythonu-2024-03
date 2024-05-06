# Získání názvu souboru od uživatele
nazev_souboru = input(
    "Zadejte název souboru, který chcete vytvořit nebo přepsat: ")

# Získání textu, který má být zapsán do souboru
text_pro_zapis = input("Zadejte řádek textu, který chcete zapsat do souboru: ")

# Otevření souboru pro zápis (přepíše soubor, pokud již existuje)
with open('reseni-cviceni/lekce-09/02-zapis-do-souboru/' + nazev_souboru + '.txt', 'w', encoding='utf-8') as soubor:
    soubor.write(text_pro_zapis + '\n')  # Přidání nového řádku na konec textu

print(f"Text byl úspěšně zapsán do souboru '{nazev_souboru}'.")
