def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + marks + "\n")

def view_students():
    with open("students.txt", "r") as file:
        print(file.read())

def search_student():
    name = input("Enter name to search: ")
    with open("students.txt", "r") as file:
        found = False   
        for line in file:
            if line.startswith(name + ","):
                print("Found:", line.strip())
                found = True
        if not found:
            print("Student not found")
while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")