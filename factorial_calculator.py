#while loop

num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial of {num} is {fact}")

#for loop
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")