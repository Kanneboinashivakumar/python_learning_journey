def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)
number = int(input("Enter a number: "))
print(f"Sum of digits: {sum_digits(number)}")