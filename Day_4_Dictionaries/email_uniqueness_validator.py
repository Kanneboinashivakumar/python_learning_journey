registered_emails = {
    "shiva@gmail.com",
    "rahul@gmail.com",
    "priya@gmail.com"
}

email = input("Enter email: ").lower()

if email in registered_emails:
    print("Email already registered")
else:
    registered_emails.add(email)
    print("Email registered successfully")