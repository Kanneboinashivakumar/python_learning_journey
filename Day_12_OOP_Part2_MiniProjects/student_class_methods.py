class Student:
    clg_name= "ABC College"

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, College: {Student.clg_name}")

    @classmethod
    def change_clg_name(cls, new_name):
        cls.clg_name = new_name

    @staticmethod
    def is_pass(marks):
        return marks >= 40
    
s1 = Student("John", 85)
s2 = Student("Jane", 70)

s1.display()
s2.display()

Student.change_clg_name("XYZ College")
print(Student.clg_name)

s1.display()
print(s1.is_pass(85))
