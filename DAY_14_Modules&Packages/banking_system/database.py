import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "accounts.txt")

def save_account(customer, account):
    with open(FILE_NAME, "a") as file:
        file.write(
            f"{customer.account_number},{customer.name},{customer.phone},{account.balance}\n"
        )

def display_accounts():
    try:
        with open(FILE_NAME, "r") as file:
            accounts = file.readlines()
            if not accounts:
                print("No accounts found.")
                return
            print("\n----- All Accounts -----")
            for line in accounts:
                account_number, name, phone, balance = line.strip().split(",")

                print(
                    f"Account No : {account_number} | "
                    f"Name : {name} | "
                    f"Phone : {phone} | "
                    f"Balance : ₹{balance}"
                )

    except FileNotFoundError:
        print("accounts.txt not found.")

def search_account(account_number):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                acc, name, phone, balance = line.strip().split(",")
                if acc == str(account_number):

                    print("\nAccount Found")
                    print("----------------------")
                    print(f"Account Number : {acc}")
                    print(f"Name           : {name}")
                    print(f"Phone          : {phone}")
                    print(f"Balance        : ₹{balance}")
                    return
            print("Account not found.")
    except FileNotFoundError:
        print("accounts.txt not found.")