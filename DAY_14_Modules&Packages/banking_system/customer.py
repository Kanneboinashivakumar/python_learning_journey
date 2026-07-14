class Customer:
    def __init__(self, account_number, name, phone):
        self.account_number = account_number
        self.name = name
        self.phone = phone
    def display(self):
        print("\n----- Customer Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Name           : {self.name}")
        print(f"Phone          : {self.phone}")