class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
    def check_pin(self, entered_pin):
        return entered_pin == self.pin
    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposited Successfully")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "Withdraw Successful")
        else:
            print("Insufficient Balance")
    def check_balance(self):
        return self.balance
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN Changed Successfully")
        else:
            print("Incorrect PIN")
atm = ATM(1234, 2000)
if atm.check_pin(1234):
    print("PIN Verified")
    atm.deposit(500)
    atm.withdraw(300)
    print("Balance:", atm.check_balance())
    atm.change_pin(1234,1122)
else:
    print("Invalid PIN")