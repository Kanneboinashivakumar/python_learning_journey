stored_username = "admin"
stored_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username:
    if password == stored_password:
        print("Login Successful ")
    else:
        print("Incorrect Password ")
else:
    print("Username not found ")