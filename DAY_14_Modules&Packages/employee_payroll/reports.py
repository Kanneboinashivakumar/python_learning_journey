FILE_NAME ="employees.txt"

def save_employee(employee):
    with open(FILE_NAME, "a") as file:
        file.write(
            f"{employee.emp_id},{employee.name},{employee.department},{employee.salary}\n"
        )

def display_employees():
    try:
        with open(FILE_NAME, "r") as file:
            employees = file.readlines()
            if not employees:
                print("No employees found.")
                return
            print("\n===== EMPLOYEE LIST =====")
            for line in employees:
                emp_id, name, department, salary = line.strip().split(",")
                print(
                    f"ID : {emp_id} | "
                    f"Name : {name} | "
                    f"Department : {department} | "
                    f"Salary : ₹{salary}"
                )
    except FileNotFoundError:
        print("employees.txt not found.")

def search_employee(emp_id):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                eid, name, department, salary = line.strip().split(",")
                if eid == str(emp_id):
                    print("\nEmployee Found")
                    print("-------------------------")
                    print(f"ID         : {eid}")
                    print(f"Name       : {name}")
                    print(f"Department : {department}")
                    print(f"Salary     : ₹{salary}")
                    return
            print("Employee not found.")
    except FileNotFoundError:
        print("employees.txt not found.")

def delete_employee(emp_id):
    try:
        with open(FILE_NAME, "r") as file:
            employees = file.readlines()
        found = False
        with open(FILE_NAME, "w") as file:
            for line in employees:
                eid = line.strip().split(",")[0]
                if eid != str(emp_id):
                    file.write(line)
                else:
                    found = True
        if found:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("employees.txt not found.")