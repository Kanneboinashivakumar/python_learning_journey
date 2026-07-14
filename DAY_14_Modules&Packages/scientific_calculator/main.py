from basic_operations import *
from scientific_operations import *
from history import save_history, view_history
from utils import get_number, get_choice


while True:

    print("\n========== SCIENTIFIC CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. View History")
    print("9. Exit")

    choice = get_choice()

    try:

        if choice == 1:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = add(a, b)
            print("Result:", result)
            save_history(f"{a} + {b} = {result}")

        elif choice == 2:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = subtract(a, b)
            print("Result:", result)
            save_history(f"{a} - {b} = {result}")

        elif choice == 3:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = multiply(a, b)
            print("Result:", result)
            save_history(f"{a} * {b} = {result}")

        elif choice == 4:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = divide(a, b)
            print("Result:", result)
            save_history(f"{a} / {b} = {result}")

        elif choice == 5:
            num = get_number("Enter number: ")
            result = square_root(num)
            print("Result:", result)
            save_history(f"√{num} = {result}")

        elif choice == 6:
            base = get_number("Enter base: ")
            exponent = get_number("Enter exponent: ")
            result = power(base, exponent)
            print("Result:", result)
            save_history(f"{base}^{exponent} = {result}")

        elif choice == 7:
            num = get_number("Enter number: ")
            result = factorial(num)
            print("Result:", result)
            save_history(f"{int(num)}! = {result}")

        elif choice == 8:
            view_history()

        elif choice == 9:
            print("Thank you for using Scientific Calculator.")
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)