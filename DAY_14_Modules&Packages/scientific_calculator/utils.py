def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_choice():
    while True:
        try:
            return int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input. Please enter a valid choice.")