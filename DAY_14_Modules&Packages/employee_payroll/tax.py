def calculate_tax(salary):
    if salary < 30000:
        return 0
    elif salary <= 50000:
        return salary * 0.05
    elif salary <= 80000:
        return salary * 0.10
    else:
        return salary * 0.20