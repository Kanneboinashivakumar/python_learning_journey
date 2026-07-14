from book import Book
from database import *
from transaction import *

while True:
    print("\n====== LIBRARY MANAGEMENT ======")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        book = Book(book_id, title, author)
        add_book(book)
        print("Book added successfully.")
    elif choice == 2:
        display_books()
    elif choice == 3:
        book_id = input("Enter Book ID: ")
        search_book(book_id)
    elif choice == 4:
        book_id = input("Enter Book ID: ")
        borrow_book(book_id)
    elif choice == 5:
        book_id = input("Enter Book ID: ")
        return_book(book_id)
    elif choice == 6:
        print("Thank you.")
        break
    else:
        print("Invalid choice.")