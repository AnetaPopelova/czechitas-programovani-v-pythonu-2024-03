class Book:
    def __init__(self, title, pages, price, sold=0, costs=0):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs

    def __str__(self):
        return f"Kniha: {self.title}, Stran: {self.pages}, Cena: {self.price} Kč, Prodané kusy: {self.sold}"

    def profit(self):
        return (self.price - self.costs) * self.sold

    def rating(self):
        zisk = self.profit()
        if zisk < 50_000:
            return "propadák"
        elif zisk <= 500_000:
            return "průměr"
        else:
            return "bestseller"

# Příklady vytvoření a použití objektů třídy Book
book1 = Book("Python Programování", 300, 450, sold=200, costs=200)
book2 = Book("Pokročilé Algoritmy", 550, 650, sold=1500, costs=250)

print(book1)
print(f"Zisk z knihy '{book1.title}': {book1.profit()} Kč")
print(f"Hodnocení knihy '{book1.title}': {book1.rating()}")

print(book2)
print(f"Zisk z knihy '{book2.title}': {book2.profit()} Kč")
print(f"Hodnocení knihy '{book2.title}': {book2.rating()}")
