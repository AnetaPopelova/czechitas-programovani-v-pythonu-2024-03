# Slovník s čísly lístků a příslušnými výhrami
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

# Zeptání uživatele na číslo jeho lístku
cislo_listku = int(input("Zadej číslo svého lístku tomboly: "))

# Kontrola, zda je číslo lístku ve slovníku
if cislo_listku in tombola:
    print("Gratulujeme! Vyhráváš:", tombola[cislo_listku])
else:
    print("Bohužel nevyhráváš nic.")
