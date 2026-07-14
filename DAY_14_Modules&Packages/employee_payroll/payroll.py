from tax import calculate_tax
class Payroll:
    def __init__(self, salary):
        self.salary = salary
    def calculate_bonus(self):
        if self.salary < 30000:
            return 2000
        elif self.salary <= 50000:
            return 5000
        else:
            return 10000
    def calculate_salary(self):
        bonus = self.calculate_bonus()
        gross_salary = self.salary + bonus
        tax = calculate_tax(gross_salary)
        net_salary = gross_salary - tax
        return gross_salary, tax, net_salary