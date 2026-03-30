# salary
salary = float(input("Enter salary: "))
#HRA (20%)
hra = 0.2 * salary
# DA (10%)
da = 0.1 * salary
# Total salary
total_salary = salary + hra + da

print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total_salary)