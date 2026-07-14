FILE_NAME = "accounts.txt"
def deposit_money(account_number, amount):
    with open(FILE_NAME, "r") as file:
        accounts = file.readlines()
    found = False
    with open(FILE_NAME, "w") as file:
        for line in accounts:
            acc, name, phone, balance = line.strip().split(",")
            if acc == str(account_number):
                balance = float(balance) + amount
                found = True
                print("Deposit Successful.")
            file.write(f"{acc},{name},{phone},{balance}\n")
    if not found:
        print("Account not found.")

def withdraw_money(account_number, amount):
    with open(FILE_NAME, "r") as file:
        accounts = file.readlines()
    found = False
    with open(FILE_NAME, "w") as file:
        for line in accounts:
            acc, name, phone, balance = line.strip().split(",")
            if acc == str(account_number):
                balance = float(balance)
                if balance >= amount:
                    balance -= amount
                    print("Withdrawal Successful.")
                else:
                    print("Insufficient Balance.")
                found = True
            file.write(f"{acc},{name},{phone},{balance}\n")
    if not found:
        print("Account not found.")

def transfer_money(from_acc, to_acc, amount):
    with open(FILE_NAME, "r") as file:
        accounts = file.readlines()
    updated_accounts = []
    sender_found = False
    receiver_found = False
    sender_balance = 0
    for line in accounts:
        acc, name, phone, balance = line.strip().split(",")
        balance = float(balance)
        if acc == str(from_acc):
            sender_found = True
            if balance >= amount:
                balance -= amount
                sender_balance = balance
            else:
                print("Insufficient Balance.")
                return
        updated_accounts.append([acc, name, phone, balance])
    for account in updated_accounts:
        if account[0] == str(to_acc):
            account[3] += amount
            receiver_found = True
    if not sender_found:
        print("Sender account not found.")
        return
    if not receiver_found:
        print("Receiver account not found.")
        return
    with open(FILE_NAME, "w") as file:
        for account in updated_accounts:
            file.write(
                f"{account[0]},{account[1]},{account[2]},{account[3]}\n"
            )
    print("Transfer Successful.")