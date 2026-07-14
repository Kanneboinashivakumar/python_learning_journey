class InvalidAgeError(Exception):
    pass
class InvalidMarksError(Exception):
    pass

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 5:
            raise InvalidAgeError("Age must be at least 5.")
        self._age = value

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        self._marks = value

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
        if self.marks >= 40:   
            print("Result: Pass")
        else:
            print("Result: Fail")

try:
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    marks = float(input("Enter student's marks: "))

    student = Student(name, age, marks)
except InvalidAgeError as e:
    print(e)
except InvalidMarksError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter numeric values for age and marks.")
else:
    student.display()
finally:
    print("Thank you for using the student result system.")