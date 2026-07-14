class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Bank:
    def __init__(self):
        self.__balance = 1000

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance
    
b = Bank()
try:
    print("=============Welcome to the ATM System==============")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        new_balance = b.deposit(amount)
        print(f"Deposit successful. New balance: {new_balance}")
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        new_balance = b.withdraw(amount)
        print(f"Withdrawal successful. New balance: {new_balance}")
    elif choice == 3:
        current_balance = b.get_balance()
        print(f"Current balance: {current_balance}")
    else:
        print("Invalid choice. Please select a valid option.")

except InvalidAmountError as e:
    print(e)    

except InsufficientFundsError as e:
    print(e)

except ValueError:
    print("Invalid input. Please enter numeric values for choice and amount.")