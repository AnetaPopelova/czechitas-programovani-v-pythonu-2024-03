from dataclasses import dataclass

@dataclass
class Item:
    title: str
    price: int

@dataclass
class Book(Item):
    pages: int

@dataclass
class AudioBook(Item):
    duration_in_hours: float
    narrator: str

# Definice oblíbeného vypravěče
favourite_narrator = "Zbyšek Horák"

# Vytvoření objektů
item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

# Seznam všech položek
all_items = [item_1, item_2, item_3]

# Projití seznamu a výpis názvů audioknih s preferovaným vypravěčem
for item in all_items:
    if hasattr(item, 'narrator') and item.narrator == favourite_narrator:
        print(item.title)
