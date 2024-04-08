# Úkol: Implementace Systému Pro Doručování

## Cíl
Váš úkol spočívá v implementaci jednoduchého systému pro doručování pizzy. 

Systém bude sledovat objednávky, včetně položek v objednávce (pizzy a nápoje), a  spravovat proces doručování.

## Popis
Systém se dělí na několik tříd, z nichž každá reprezentuje různé aspekty procesu doručování: položky (pizzy a nápoje), objednávky a doručovatelé.

### Část 1: Třídy Položka, Pizza a Nápoj

#### Třída Položka (Item)
- Jedná se o základní třídu pro všechny položky, které lze objednat.
   - Měla by mít dva atributy: `name` (řetězec reprezentující název položky) a `price` (float reprezentující cenu položky).
   - Implementujte metodu `__str__` tak, aby vracela řetězcovou reprezentaci položky ve formátu: `<název>: <cena> Kč`.

- **Atributy**:
  - `name`: Název položky (string).
  - `price`: Cena položky (float).
- **Metody**:
  - `__str__()`: Vrací řetězcovou reprezentaci položky.

#### Třída Pizza (dědí z Item)
- Reprezentuje pizzu, která je specifickým typem položky.
   - Přidává dodatečný atribut: `ingredients` (slovník, kde klíče jsou názvy ingrediencí a hodnoty jejich množství v gramech).
   - Implementujte metodu `add_extra` pro přidání extra ingrediencí do pizzy. Tato metoda by měla odpovídajícím způsobem aktualizovat cenu pizzy.
   - Napište metodu `__str__` tak, aby zahrnovala seznam ingrediencí a celkovou cenu.

- **Atributy**:
  - `ingredients`: Slovník ingrediencí a jejich množství (dict).
- **Metody**:
  - `add_extra(ingredient, quantity, price_per_ingredient)`: Přidává extra ingredienci do pizzy a aktualizuje její cenu.
  - `__str__()`: Vrací textový popis pizzy včetně ingrediencí a ceny.

#### Třída Drink (dědí z Item)
- Reprezentuje nápoj.
   - Přidává dodatečný atribut: `volume` (integer reprezentující objem nápoje v mililitrech).
   - Přepište metodu `__str__` tak, aby vracela název nápoje, objem a cenu.

- **Atributy**:
  - `volume`: Objem nápoje v mililitrech (int).
- **Metody**:
  - `__str__()`: Vrací popis nápoje, včetně jeho objemu a ceny.

### Část 2: Třída Order
- Reprezentuje objednávku učiněnou zákazníkem.
  - Měla by obsahovat jméno zákazníka, adresu doručení, seznam objednaných položek a stav objednávky (např. "Nová", "Doručeno").
  - Implementujte metodu `mark_delivered`, která změní stav objednávky na "Doručeno".
  - Přepište metodu `__str__` tak, aby vracela podrobné informace o objednávce, včetně jména zákazníka, adresy, položek v objednávce a stavu objednávky.
- **Atributy**:
  - `customer_name`: Jméno zákazníka (string).
  - `delivery_address`: Adresa doručení (string).
  - `items`: Seznam položek v objednávce (list).
  - `status`: Stav objednávky (string).
- **Metody**:
  - `mark_delivered()`: Označí objednávku jako doručenou.
  - `__str__()`: Vrací detaily objednávky, včetně zákazníka, adresy, položek a stavu.

### Část 3: Třída DeliveryPerson
- Reprezentuje doručovatele.
 - Měla by obsahovat jméno doručovatele, telefonní číslo, stav dostupnosti a aktuální objednávku, kterou doručuje (pokud nějakou má).
 - Implementujte metodu `assign_order`, která přiřadí objednávku doručovateli, pokud je dostupný. Stav objednávky by měl být aktualizován na "Na cestě".
 - Implementujte metodu `complete_delivery`, která označí objednávku jako doručenou a doručovatele znovu učiní dostupným pro nové objednávky.
 - Přepište metodu `__str__` tak, aby vracela informace o doručovateli, včetně jeho stavu dostupnosti.

- **Atributy**:
  - `name`: Jméno doručovatele (string).
  - `phone_number`: Telefonní číslo doručovatele (string).
  - `available`: Dostupnost doručovatele (bool).
  - `current_order`: Aktuální objednávka k doručení (Order).
- **Metody**:
  - `assign_order(order)`: Přiřadí objednávku doručovateli, pokud je dostupný.
  - `complete_delivery()`: Označí objednávku jako doručenou a doručovatele znovu učiní dostupným.
  - `__str__()`: Vrací informace o doručovateli, včetně jeho stavu dostupnosti.

### Příklad Použití
```py
# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1.5, 500)

# Vytvoření a výpis objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person)

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)
```