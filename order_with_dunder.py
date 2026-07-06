class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
         return self.price > ord2.price  

ord1 = Order("Laptop", 100000)
ord2 = Order("Mobile", 50000)
print(ord1 > ord2)  # Output: True