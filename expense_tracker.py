expenses = {
    "Food": 2500,
    "Transport": 1200,
    "Shopping": 4000,
    "Internet": 800,
    "Electricity": 1800
}

total_expense = sum(expenses.values())

highest_category = max(expenses, key=expenses.get)

print("Total Expense:", total_expense)
print("Highest Expense Category:", highest_category)
print("Amount:", expenses[highest_category])