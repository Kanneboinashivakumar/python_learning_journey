class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Book Added:", book.title)
    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print("-", book.title)
    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book Issued:", title)
                return
        print("Book not available")
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book Returned:", title)
                return
lib = Library()
b1 = Book("Python Basics", "Guido")
b2 = Book("Java Fundamentals", "James")
lib.add_book(b1)
lib.add_book(b2)
lib.show_books()
lib.issue_book("Python Basics")
lib.show_books()
lib.return_book("Python Basics")
lib.show_books()