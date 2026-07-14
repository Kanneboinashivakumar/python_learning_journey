print("===== SMART CALCULATOR =====")
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    else:
        raise ValueError("Invalid operation. Please enter one of +, -, *, /.")

except ValueError as e:
    print(e)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)

finally:
    print("Thank you for using the smart calculator.")