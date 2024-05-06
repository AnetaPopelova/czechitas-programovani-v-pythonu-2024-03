# Seznam knih
knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

# Pokus o načtení knihy zadaného indexu s ošetřením chyby
try:
    index = int(input("Zadej index knihy: "))
    print("Vybraná kniha:", knihy[index])
# except ValueError:
#     print("Chyba: Nebylo zadáno platné číslo.")
except IndexError:
    print("Chyba: Zadaný index je mimo rozsah seznamu.")
