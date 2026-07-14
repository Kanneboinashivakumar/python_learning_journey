filename = "history.txt"
def save_history(operation):
    with open(filename, "a") as file:
        file.write(operation + "\n")

def view_history():
    try:
        with open(filename, "r") as file:
            history = file.readlines()
            if not history:
                print("No history available.")
            else:
                print("Calculation History:")
                for entry in history:
                    print(entry.strip())
    except FileNotFoundError:
        print("No history available.")