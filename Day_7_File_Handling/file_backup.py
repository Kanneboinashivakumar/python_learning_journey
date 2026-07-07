try:
    with open("source.txt", "r") as source:
        data = source.read()
    with open("backup.txt", "w") as backup:
        backup.write(data)
    print("Backup created successfully")
except FileNotFoundError:
    print("Source file not found")