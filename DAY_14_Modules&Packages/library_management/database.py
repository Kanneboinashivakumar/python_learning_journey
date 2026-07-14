from book import Book
FILE_NAME = "books.txt"
def add_book(book):
    with open(FILE_NAME, "a") as file:
        file.write(
            f"{book.book_id},{book.title},{book.author},{book.available}\n"
        )

def display_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()
            if not books:
                print("No books found.")
                return
            for line in books:
                book_id, title, author, available = line.strip().split(",")
                book = Book(
                    book_id,
                    title,
                    author,
                    available == "True"
                )
                book.display()
    except FileNotFoundError:
        print("Books file not found.")

def search_book(book_id):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                bid, title, author, available = line.strip().split(",")
                if bid == str(book_id):
                    Book(
                        bid,
                        title,
                        author,
                        available == "True"
                    ).display()
                    return
            print("Book not found.")
    except FileNotFoundError:
        print("Books file not found.")