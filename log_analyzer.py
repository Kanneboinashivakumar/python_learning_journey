with open("log.txt", "r") as file:
    lines = file.readlines()
    print(lines)
print(len(lines))
print("ERROR LOGS:\n")
for line in lines:
    if "ERROR" in line:
        print(line.strip())