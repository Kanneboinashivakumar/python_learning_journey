users = {
    "user1": "pass123",
    "admin": "admin@123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Credentials")