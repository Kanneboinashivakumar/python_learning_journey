nums = list(map(int, input("Enter numbers separated by space: ").split()))

choice = input("Enter even/odd: ")

result = []

for num in nums:
    if choice == "even" and num % 2 == 0:
        result.append(num)
    elif choice == "odd" and num % 2 != 0:
        result.append(num)

print(result) 