from student import Student
from validation import *
from file_handler import *
from menu import show_menu

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))
            validate_student_id(student_id)
            validate_name(name)
            validate_age(age)
            validate_marks(marks)
            student = Student(student_id, name, age, marks)
            save_student(student)
            print("Student added successfully.")
        elif choice == 2:
            student_id = int(input("Enter Student ID: "))
            search_student(student_id)
        elif choice == 3:
            student_id = int(input("Enter Student ID: "))
            marks = float(input("Enter New Marks: "))
            validate_marks(marks)
            update_student(student_id, marks)
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            delete_student(student_id)
        elif choice == 5:
            display_students()
        elif choice == 6:
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(e)