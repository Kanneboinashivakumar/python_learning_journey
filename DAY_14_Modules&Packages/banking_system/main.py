import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from customer import Customer
from account import Account
from database import *
from validation import *
from transaction import *

while True:
    print("\n========== BANKING SYSTEM ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer Money")
    print("5. Search Account")
    print("6. Display All Accounts")
    print("7. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            account_number = int(input("Enter Account Number: "))
            name = input("Enter Customer Name: ")
            phone = input("Enter Phone Number: ")
            balance = float(input("Enter Initial Balance: "))
            validate_account(account_number)
            validate_phone(phone)
            validate_amount(balance)
            customer = Customer(account_number, name, phone)
            account = Account(balance)
            save_account(customer, account)
            print("Account Created Successfully.")
        elif choice == 2:
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Amount: "))
            validate_amount(amount)
            deposit_money(account_number, amount)
        elif choice == 3:
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Amount: "))
            validate_amount(amount)
            withdraw_money(account_number, amount)
        elif choice == 4:
            sender = int(input("Sender Account Number: "))
            receiver = int(input("Receiver Account Number: "))
            amount = float(input("Amount: "))
            validate_amount(amount)
            transfer_money(sender, receiver, amount)
        elif choice == 5:
            account_number = int(input("Enter Account Number: "))
            search_account(account_number)
        elif choice == 6:
            display_accounts()
        elif choice == 7:
            print("Thank you for using Banking Management System.")
            break
        else:
            print("Invalid Choice.")
    except Exception as e:
        print(e)