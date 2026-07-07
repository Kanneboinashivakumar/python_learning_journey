contacts = [("Shiva", 9876), ("Ram", 1234)]
index = int(input("Enter index: "))
print(contacts[index])
if index >= 0 and index < len(contacts):
    contact = contacts[index]
    print(f"Name: {contact[0]}")
    print(f"Phone: {contact[1]}")
else:
    print("Invalid index")