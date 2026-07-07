num = list(map(int, input().split(",")))
min = num[0]
max = num[0]

for i in num:
    if i < min:
        min = i
    if i > max:
        max = i
print(f"Maximum:{max} and Minimum:{min}")

#another way
num = list(map(int, input().split(",")))
num.sort()
print(f"Maximum: {num[-1]} and Minimum: {num[0]}")