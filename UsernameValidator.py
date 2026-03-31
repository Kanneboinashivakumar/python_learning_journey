username = input("Enter username: ")
if len(username) > 5 and " " not in username and username[0].isalpha():
    print("Valid Username ")
else:
    print("Invalid Username ")

