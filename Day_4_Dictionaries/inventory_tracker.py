inventory = {
    "apple": 20,
    "banana": 15,
    "milk": 8,
    "bread": 10,
    "rice": 25
}

item = input("Enter item name: ").lower()

if item in inventory:
    print("Item Available")
    print("Quantity:", inventory[item])
else:
    print("Item not available")