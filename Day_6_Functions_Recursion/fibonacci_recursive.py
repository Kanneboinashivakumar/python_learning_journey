def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    print(f"Fibonacci({number}) = {fibonacci(number)}")