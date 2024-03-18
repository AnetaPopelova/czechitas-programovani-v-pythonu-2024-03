def total_price(persons, breakfast=False):
    cena_noci = 850  # Cena za noc za osobu
    cena_snidane = 125  # Cena za snídani za osobu

    celkova_cena_noci = persons * cena_noci

    if breakfast:
        celkova_cena_noci += persons * cena_snidane

    return celkova_cena_noci

# Testování funkce
print("Cena za pobyt bez snídaně pro 3 osoby:", total_price(3))
print("Cena za pobyt s snídaní pro 2 osoby:", total_price(2, True))
