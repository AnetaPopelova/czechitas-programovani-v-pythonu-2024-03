class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def get_time_to_read(self):
        pass

class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages
    
    def get_time_to_read(self):
        # Předpokládáme průměrnou rychlost čtení 1 strana / 4 minuty
        return self.pages * 4 / 60  # Vrací čas v hodinách

class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator
    
    def get_time_to_read(self):
        return self.duration_in_hours

# Vytvoření objektů
audiobook = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
book = Book("Kadet Hornblower", 399, 242)

# Výpočet celkového času
total_time = audiobook.get_time_to_read() + book.get_time_to_read()

print(f"Celkový čas na užívání produktů je {total_time} hodin.")
