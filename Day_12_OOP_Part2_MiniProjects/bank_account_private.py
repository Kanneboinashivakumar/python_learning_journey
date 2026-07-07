from datetime import datetime

class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.__account_number = account_number
        self.__balance = balance
        self.__account_holder = account_holder

    def __show_transaction(self, message):
        timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        print(f"[{timestamp}] {message}")

    def deposit(self, amount):
        self.__balance += amount
        self.__show_transaction(
            f"Deposited: {amount}. New balance: {self.__balance}"
        )

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__show_transaction(
                f"Withdrawn: {amount}. New balance: {self.__balance}"
            )
        else:
            self.__show_transaction("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.__balance
    
account = BankAccount("123456789", 1000, "John Doe")
account.deposit(500)
account.withdraw(200)
print(f"Current balance: {account.get_balance()}")