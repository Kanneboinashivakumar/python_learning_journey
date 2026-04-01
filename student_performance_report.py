students = [("Shiva", 85), ("Ram", 92), ("Ravi", 78)]
topper = max(students, key=lambda x: x[1])
lowest = min(students, key=lambda x: x[1])
print(f"Topper: {topper[0]} ({topper[1]})")
print(f"Lowest: {lowest[0]} ({lowest[1]})")
s1 = students[0]
s2 = students[1]
if s1[1] > s2[1]:
    print(f"{s1[0]} scored higher than {s2[0]}")
elif s1[1] < s2[1]:
    print(f"{s2[0]} scored higher than {s1[0]}")
else:
    print("Both scored equal")