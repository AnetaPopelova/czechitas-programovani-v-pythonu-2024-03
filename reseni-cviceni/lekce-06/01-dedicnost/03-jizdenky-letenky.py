class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

    def get_price(self):
        if self.fare_class == 'economy':
            return self.basic_price
        elif self.fare_class == 'business':
            return self.basic_price * 1.3  # Cena o 30 % vyšší

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        price = super().get_price()
        if self.fare_class == 'business':
            price = self.basic_price * 1.5  # Cena o 50 % vyšší pro business class
        return price + (2000 * self.checkout_luggages)  # Připočet 2000 za každé zavazadlo

# Vytvoření jízdenek na vlak
train_ticket_economy = TrainTicket(150, "12A", "economy")
train_ticket_business = TrainTicket(150, "1B", "business")

# Vytvoření letenek
plane_ticket_economy = PlaneTicket(6000, "20A", "economy", 1)
plane_ticket_business = PlaneTicket(6000, "1A", "business", 1)

# Výpis cen
print("Cena jízdenky na vlak (economy):", train_ticket_economy.get_price())
print("Cena jízdenky na vlak (business):", train_ticket_business.get_price())
print("Cena letenky (economy):", plane_ticket_economy.get_price())
print("Cena letenky (business):", plane_ticket_business.get_price())

# Vypočítání celkové ceny dvou jízdenek
total_price = train_ticket_economy.get_price() + plane_ticket_business.get_price()
print("Celková cena jízdenky na vlak (economy) a letenky (business):", total_price)
