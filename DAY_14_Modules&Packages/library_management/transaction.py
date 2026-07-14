FILE_NAME = "books.txt"
def borrow_book(book_id):
    with open(FILE_NAME, "r") as file:
        books = file.readlines()
    with open(FILE_NAME, "w") as file:
        found = False
        for line in books:
            bid, title, author, available = line.strip().split(",")
            if bid == str(book_id):
                if available == "False":
                    print("Book already issued.")
                else:
                    available = "False"
                    print("Book borrowed successfully.")
                found = True
            file.write(f"{bid},{title},{author},{available}\n")
        if not found:
            print("Book not found.")
def return_book(book_id):
    with open(FILE_NAME, "r") as file:
        books = file.readlines()
    with open(FILE_NAME, "w") as file:
        found = False
        for line in books:
            bid, title, author, available = line.strip().split(",")
            if bid == str(book_id):
                available = "True"
                print("Book returned successfully.")
                found = True
            file.write(f"{bid},{title},{author},{available}\n")
        if not found:
            print("Book not found.")