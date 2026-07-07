email = input("Enter email: ")
if "@" in email and "." in email and email[0] != "@":
    print("Valid Email ")
else:
    print("Invalid Email ")