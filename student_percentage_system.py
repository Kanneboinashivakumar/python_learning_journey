class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)
    
student1 = Student("John", [85, 90, 78])
print(f"{student1.name}'s percentage: {student1.percentage()}%")

student1.marks[0] = 95
print(f"After updating marks, {student1.name}'s percentage: {student1.percentage()}%")