# Existující slovník s prodeji
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Přidání nové knihy s nulovým počtem prodejů
sales["Noc, která mě zabila"] = 0

# Zvýšení počtu prodaných kusů u knihy "Vrah zavolá v deset"
sales["Vrah zavolá v deset"] += 100

# Vypsání upraveného slovníku
print(sales)
