import json

# Načtení souboru JSON
with open(
    "reseni-cviceni/lekce-10/02-cteni-na-doma/kurz.json", "r", encoding="utf-8"
) as file:
    data = json.load(file)

# Data kurzu
konani = data["konani"]

# 1. Počet účastnic na posledním konání kurzu
pocet_ucastnic_posledni = konani[-1]["ucastnic"]
print("Počet účastnic na posledním konání kurzu:", pocet_ucastnic_posledni)

# 2. Jméno posledního kouče na prvním konání kurzu
jmeno_posledniho_kouce_prvni = konani[0]["koucove"][-1]
print("Jméno posledního kouče na prvním konání kurzu:", jmeno_posledniho_kouce_prvni)

# 3. Celkový počet konání kurzu
celkovy_pocet_konani = len(konani)
print("Celkový počet konání kurzu:", celkovy_pocet_konani)

# 4. Všechna místa, na kterých se kurz konal
mista = set(k["misto"] for k in konani)
print("Všechna místa, na kterých se kurz konal:", ", ".join(mista))

# 5. Součet všech účastnic
soucet_ucastnic = sum(k["ucastnic"] for k in konani)
print("Součet všech účastnic:", soucet_ucastnic)

# 6. Množina všech koučů, kteří se kdy kurzu účastnili
kouci = set(kouc for k in konani for kouc in k["koucove"])
print("Množina všech koučů, kteří se kdy kurzu účastnili:", ", ".join(kouci))
