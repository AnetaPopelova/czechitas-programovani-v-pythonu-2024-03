from datetime import datetime, timedelta

cas_objednavky = datetime(2022, 4, 25, 19, 47)

doba_prevzeti = timedelta(minutes=8, seconds=35)
doba_pripravy = timedelta(minutes=30)
doba_dopravy = timedelta(minutes=25, seconds=30)

cas_dodani = cas_objednavky + doba_prevzeti + doba_pripravy + doba_dopravy
cas_dodani = cas_dodani.strftime("%H:%M:%S")
print(cas_dodani)
