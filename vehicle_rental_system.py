class Vehicle:
    def __init__(self, brand,rent):
        self.brand = brand
        self.rent = rent

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Rental Price: ${self.rent}/day")

class Car(Vehicle):
    def __init__(self, brand, rent, seats):
        super().__init__(brand, rent)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}")

car1 = Car("Toyota", 50, 5)
car1.display_info()  