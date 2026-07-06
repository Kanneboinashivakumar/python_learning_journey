class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
    def add_stock(self, additional_quantity):
        self.quantity += additional_quantity

    def sell(self, sold_quantity):
        if sold_quantity <= self.quantity:
            self.quantity -= sold_quantity
        else:
            print("Not enough stock available.")

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
p=Product("Laptop", 1000, 10)
print(p)
p.sell(3)
print(p)
p.add_stock(5)  
print(p)
print(f"Total value of {p.name} in stock: ${p.total_value()}")