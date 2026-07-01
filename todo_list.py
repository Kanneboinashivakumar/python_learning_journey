while True:

    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        task = input("Enter task: ")

        with open("todo.txt", "a") as file:
            file.write(task + "\n")

    elif choice == "2":

        with open("todo.txt", "r") as file:
            print("\nTasks:")
            print(file.read())

    elif choice == "3":
        break

    else:
        print("Invalid choice")