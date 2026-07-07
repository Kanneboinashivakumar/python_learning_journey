students = {"Shiva": 85, "Ram": 90}

name = input("Enter name: ")

if name in students:
    print(f"Marks: {students[name]}")
else:
    print("Student not found")