def decimal_to_binary(num):
    if num == 0:
        return ""

    return decimal_to_binary(num // 2) + str(num % 2)

number = int(input("Enter a decimal number: "))

if number == 0:
    print("Binary: 0")
else:
    print(f"Binary: {decimal_to_binary(number)}")