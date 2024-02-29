def spocitej_pokutu(pocet_naprav, hmotnost):
    if pocet_naprav == 2:
        limit = 18
    elif pocet_naprav == 3:
        limit = 25
    elif pocet_naprav == 4:
        limit = 32
    elif pocet_naprav == 5:
        limit = 48
    else:
        return "Neplatný počet náprav"

    if hmotnost > limit:
        return (hmotnost - limit) * 1000
    else:
        return 0

vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]

celkova_pokuta = 0

for vazeni_item in vazeni:
    pocet_naprav = vazeni_item[0]
    hmotnost = vazeni_item[1]
    pokuta = spocitej_pokutu(pocet_naprav, hmotnost)
    celkova_pokuta += pokuta
    print("Pokuta za vážení s", pocet_naprav, "nápravami a hmotností", hmotnost, "tun:", pokuta)

print("Celková výše pokut za všechna vážení:", celkova_pokuta)
