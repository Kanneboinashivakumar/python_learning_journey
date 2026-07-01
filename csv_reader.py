total = 0
count = 0
with open("students.csv", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        marks = int(marks)
        print("Name:", name, "Marks:", marks)
        total += marks
        count += 1
print("\nTotal Marks:", total)
print("Average:", total / count)