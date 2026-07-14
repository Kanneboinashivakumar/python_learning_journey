from employee import Employee
from attendance import Attendance
from payroll import Payroll
from reports import *

while True:
    print("\n========== EMPLOYEE PAYROLL ==========")
    print("1. Add Employee")
    print("2. Calculate Payroll")
    print("3. Search Employee")
    print("4. Display Employees")
    print("5. Delete Employee")
    print("6. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            emp_id = input("Employee ID: ")
            name = input("Employee Name: ")
            department = input("Department: ")
            salary = float(input("Basic Salary: "))
            employee = Employee(emp_id, name, department, salary)
            save_employee(employee)
            print("Employee added successfully.")
        elif choice == 2:
            salary = float(input("Enter Employee Salary: "))
            attendance = Attendance()
            attendance.mark_attendance()
            payroll = Payroll(salary)
            gross, tax, net = payroll.calculate_salary()
            print("\n========== PAYROLL REPORT ==========")
            attendance.display()
            print(f"Basic Salary : ₹{salary}")
            print(f"Bonus        : ₹{payroll.calculate_bonus()}")
            print(f"Gross Salary : ₹{gross}")
            print(f"Tax          : ₹{tax}")
            print(f"Net Salary   : ₹{net}")
        elif choice == 3:
            emp_id = input("Enter Employee ID: ")
            search_employee(emp_id)
        elif choice == 4:
            display_employees()
        elif choice == 5:
            emp_id = input("Enter Employee ID: ")
            delete_employee(emp_id)
        elif choice == 6:
            print("Thank you.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid input.")