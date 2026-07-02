class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposited")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "Withdrawn")
        else:
            print("Insufficient Balance")
    def show_balance(self):
        return self.balance
a1 = Account("Shiva", 1000)
a1.deposit(500)
a1.withdraw(200)
print("Balance:", a1.show_balance())