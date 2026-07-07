class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
    def result(self):
        if self.average() >= 40:
            return "Pass"
        else:
            return "Fail"
s1 = Student("Shiva", 85, 90, 88)
print("Name:", s1.name)
print("Average:", s1.average())
print("Result:", s1.result())