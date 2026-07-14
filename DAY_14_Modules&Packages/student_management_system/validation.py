def validate_student_id(student_id):
    if student_id <=0:
        raise ValueError("Student ID must be a positive integer.")
    
def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")

def validate_age(age):
    if age <5 or age > 100:
        raise ValueError("Age must be between 5 and 100.")

def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")