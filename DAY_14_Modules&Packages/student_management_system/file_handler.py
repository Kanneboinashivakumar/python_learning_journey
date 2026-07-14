from student import Student
FILE_NAME = "data.txt"
def save_student(student):
    with open(FILE_NAME, "a") as file:
        file.write(f"{student.student_id},{student.name},{student.age},{student.marks}\n")
def display_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
            if not data:
                print("No student records found.")
                return
            print("\n----- Student Records -----")
            for line in data:
                student_id, name, age, marks = line.strip().split(",")
                student = Student(student_id, name, age, marks)
                student.display()
    except FileNotFoundError:
        print("Student record file not found.")

def search_student(student_id):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                sid, name, age, marks = line.strip().split(",")
                if sid == str(student_id):
                    student = Student(sid, name, age, marks)
                    student.display()
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("Student record file not found.")

def delete_student(student_id):
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
        with open(FILE_NAME, "w") as file:
            found = False
            for line in students:
                sid = line.strip().split(",")[0]
                if sid != str(student_id):
                    file.write(line)
                else:
                    found = True
        if found:
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("Student record file not found.")
def update_student(student_id, new_marks):
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
        with open(FILE_NAME, "w") as file:
            found = False

            for line in students:
                sid, name, age, marks = line.strip().split(",")
                if sid == str(student_id):
                    file.write(f"{sid},{name},{age},{new_marks}\n")
                    found = True
                else:
                    file.write(line)
        if found:
            print("Student updated successfully.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("Student record file not found.")