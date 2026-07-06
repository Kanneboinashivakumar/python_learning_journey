class employee:
    def __init__(self, role, department, salary):
        self.role = role    
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class engineer(employee):
    def __init__(self, name,age ):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Development", 60000)

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_details()

e1 = engineer("John", 30)
e1.show_details()