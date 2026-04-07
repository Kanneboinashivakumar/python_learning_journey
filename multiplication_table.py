num = int(input("Enter number: "))
limit = int(input("Enter range: "))

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")