from datetime import datetime

# Ulož si hodnotu startu do proměnné.
start_Solar_Orbiter = datetime(2020, 2, 10, 5, 3)

# Který den v týdnu Solar Orbiter odstartoval?
den_v_tydnu = start_Solar_Orbiter.weekday()
print(f"Solar Orbiter odstartoval v {den_v_tydnu}")

den_v_tydnu = start_Solar_Orbiter.strftime("%A")
print(f"Solar Orbiter odstartoval v {den_v_tydnu}")

# Spočítej, kolik času od jeho startu uplynulo.
aktualni_cas = datetime.now()

cas_od_startu = aktualni_cas - start_Solar_Orbiter
print(cas_od_startu)
