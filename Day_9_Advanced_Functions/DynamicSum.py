n = int(input("Enter number of subjects: "))
total = 0
for i in range(n):
    marks = int(input(f"Enter marks of subject {i+1}: "))
    total = total + marks
average = total / n
print("Total Marks =", total)
print("Average Marks =", average)

#using functions

def dynamic_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# Function Call
result = dynamic_sum(10, 20, 30, 40, 50)

print("Numbers: 10, 20, 30, 40, 50")
print("Total Sum:", result)