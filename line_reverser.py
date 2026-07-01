with open("input.txt", "r") as file:
    lines = file.readlines()
lines.reverse()
with open("output.txt", "w") as file:
    file.writelines(lines)
print("Lines reversed successfully")