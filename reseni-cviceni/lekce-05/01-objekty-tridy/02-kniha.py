class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Kniha: {self.title}, Počet stran: {self.pages}, Cena: {self.price} Kč."

    def get_time_to_read(self, minutes_per_page=4):
        total_minutes = self.pages * minutes_per_page
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"Čas potřebný na přečtení: {hours} hodin a {minutes} minut."

# Příklady použití
book1 = Book("Python Programování", 250, 399)
book2 = Book("Pokročilé Algoritmy", 500, 799)

print(book1.get_info())
print(book1.get_time_to_read())

print(book2.get_info())
print(book2.get_time_to_read(5))  # Předpokládáme, že čtenář potřebuje 5 minut na stránku

