# Approach:
# 1. Take year as input.
# 2. If year is divisible by 400 → Leap Year.
# 3. Else if year is divisible by 100 → Not a Leap Year.
# 4. Else if year is divisible by 4 → Leap Year.
# 5. Otherwise → Not a Leap Year.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")