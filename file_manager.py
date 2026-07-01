import os
filename = "notes.txt"
with open("practice.txt", "w+") as file:
    file.write("Hello Python!")
    file.seek(0)
    print(f"Current position: {file.read()}")
if os.path.exists(filename):
    print("File exists")
os.rename("practice.txt", "my_notes.txt")
print("File renamed successfully")
os.remove("my_notes.txt")
print("File deleted successfully")