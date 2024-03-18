# Vytvoření prázdného slovníku
slovnik = {}
# Vytiskne typ proměnné 'slovnik', což je <class 'dict'>
print(type(slovnik))

# Definice slovníku 'item' s klíči 'title', 'price' a 'in_stock'
item = {"title": "Čajová konvice", 
        "price": 899, 
        "in_stock": True}
# Vytiskne hodnotu asociovanou s klíčem 'title' v slovníku 'item'
print(item["title"])

# Přidání nového klíče 'weight' s hodnotou 0.5 do slovníku 'item'
item["weight"] = 0.5
# Vytiskne celý slovník 'item' s přidaným klíčem 'weight'
print(item)

# Aktualizace hodnoty klíče 'price' na 999 v slovníku 'item'
item["price"] = 999
# Vytiskne slovník 'item' s aktualizovanou hodnotou 'price'
print(item)

# Definice slovníku 'sales' s názvy knih a prodanými kusy
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Procházení slovníku 'sales' a výtisk názvů knih (klíčů)
for k in sales:
    print(k)

# Inicializace proměnné 'total_sales' pro součet všech prodejů
total_sales = 0

# Procházení slovníku 'sales', sčítání prodejů a tisk klíčů s hodnotami
for key, value in sales.items():
    total_sales += value
    print(key, value)
# Vytiskne celkový počet prodaných kusů
print(total_sales)

# Vytiskne všechny klíče v slovníku 'sales'
print(sales.keys())
# Vytiskne všechny hodnoty v slovníku 'sales'
print(sales.values())
