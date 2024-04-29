# import datetime as dt
# print(dt.datetime.now())

# Importování tříd z modulu datetime
from datetime import datetime, timedelta, date

# Výpis aktuálního datumu a času
print(datetime.now())

# Alternativní metoda pro získání dnešního datumu a času
print(datetime.today())

# Výpis pouze dnešního data
print(date.today())

# Vytvoření objektu datetime pro konkrétní datum a čas
muj_udaj = datetime(2024, 5, 1, 13, 00)
print(muj_udaj)

# Výpis čísla dne v týdnu (pondělí=0, neděle=6)
print(muj_udaj.weekday())

# Výpis čísla dne v týdnu podle ISO (pondělí=1, neděle=7)
print(muj_udaj.isoweekday())

# Výpis data a času ve formátu ISO 8601
print(muj_udaj.isoformat())

# Formátovaný výpis data a času
print(muj_udaj.strftime("%d. %m. %Y, %H:%M"))

# Výpis názvu dne v týdnu
print(muj_udaj.strftime("%A"))

# Převod řetězce ve formátu ISO 8601 zpět na objekt datetime
retezec_iso = "2024-05-01T13:00:00"
print(datetime.fromisoformat(retezec_iso))

# Převod řetězce s konkrétním formátem na objekt datetime
retezec = "1. 5. 2024, 18:38"
print(datetime.strptime(retezec, "%d. %m. %Y, %H:%M"))

# Uložení dnešního datumu a výpočet včerejšího data
dnes = datetime.today()
vcera = dnes - timedelta(days=1)
print(dnes, vcera)

# Výpočet rozdílu od data narození do dnešního dne
datum_narozeni = datetime(1950, 12, 24)
print(datetime.today() - datum_narozeni)

# Vytvoření objektu timedelta a výpočet celkového počtu sekund
hodnota_timedelta = timedelta(days=10_000, hours=23, seconds=3)
print(hodnota_timedelta.total_seconds())
