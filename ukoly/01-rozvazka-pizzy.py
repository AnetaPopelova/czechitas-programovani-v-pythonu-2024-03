class Item:
    def __init__(self, name, price):
        """Inicializuje položku s názvem a cenou."""
        self.name = name
        self.price = price

    def __str__(self):
        """Vrací textový popis položky."""
        return f"{self.name}: {self.price} Kč"

class Pizza(Item):
    def __init__(self, name, price, ingredients):
        """Inicializuje pizzu s názvem, cenou a slovníkem ingrediencí."""
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        """Přidává extra ingredienci do pizzy."""
        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += price_per_ingredient * quantity

    def __str__(self):
        """Vrací textový popis pizzy včetně jejích ingrediencí a ceny."""
        ingredients_list = ', '.join([f"{key}: {value}g" for key, value in self.ingredients.items()])
        return f"Pizza {self.name} - Ingredients: {ingredients_list}. Price: {self.price} Kč"

class Drink(Item):
    def __init__(self, name, price, volume):
        """Inicializuje nápoj s názvem, cenou a objemem."""
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        """Vrací textový popis nápoje."""
        return f"{self.name}: {self.volume}ml - {self.price} Kč"

class Order:

    def __init__(self, customer_name, delivery_address, items=None):
        """Inicializuje objednávku s jménem zákazníka, adresou a seznamem položek."""
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová"

    def mark_delivered(self):
        """Označí objednávku jako doručenou."""
        self.status = "Doručeno"

    def __str__(self):
        """Vrací detaily objednávky včetně zákazníka, adresy, položek a stavu."""
        items_list = '\n'.join([str(item) for item in self.items])
        return f"Objednávka pro {self.customer_name}, Adresa: {self.delivery_address}\n" \
               f"Obsah objednávky:\n{items_list}\nStav: {self.status}"


class DeliveryPerson:
    def __init__(self, name, phone_number):
        """Inicializuje řidiče s jménem a telefonním číslem."""
        self.name = name
        self.phone_number = phone_number
        self.available = True
        self.current_order = None

    def assign_order(self, order):
        """Přiřadí objednávku k doručení, pokud je řidič dostupný."""
        if self.available:
            self.current_order = order
            self.available = False
            order.status = "Na cestě"
            print(f"Objednávka přiřazena řidiči {self.name}.")
        else:
            print("Řidič není dostupný.")

    def complete_delivery(self):
        """Označí objednávku jako doručenou a řidiče znovu jako dostupného."""
        if self.current_order:
            self.current_order.mark_delivered()
            self.current_order = None
            self.available = True
            print("Doručení dokončeno.")

    def __str__(self):
        """Vrací informace o řidiči."""
        status = "Dostupný" if self.available else "Nedostupný"
        return f"Řidič: {self.name}, Telefon: {self.phone_number}, Stav: {status}"

# Příklady použití
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

