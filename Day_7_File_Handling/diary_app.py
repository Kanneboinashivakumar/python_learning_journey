while True:
    print("\n1.Write Entry")
    print("2.View Diary")
    print("3.Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        note = input("Enter today's note: ")
        with open("diary.txt", "a") as file:
            file.write(note + "\n")
    elif choice == "2":
        with open("diary.txt", "r") as file:
            print(file.read())
    elif choice == "3":
        break
    else:
        print("Invalid choice")