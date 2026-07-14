class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print (f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}")