# Book operation module containing book operations menu and user interaction
from book_class import Book
import re

library = []

# Defining a function to display all books in 'library' list with their details
def display_books(library):
    if library:
        print("Library:")
        for book in library:
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Publication Date: {book.get_publication()}, Availability Status: {book.get_availability()}")
    else:
        print("Library contains no books.")

# Defining a function to display book operations menu and enable user interaction
def display_book_menu():
    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    user_input = input("Enter your choice: ").strip()
    if user_input == '1':
        title_input = input("Enter the book's title: ").title()
        author_input = input("Enter the book's author: ").title()
        genre_input = input("Enter the book's genre: ").title()
        publication_input = input("Enter the book's publication date (mm/dd/yyyy): ")
        if title_input not in [book.get_title() for book in library]:
            if re.findall(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$", publication_input):
                new_book = Book(title_input, author_input, genre_input, publication_input)
                new_book.add_book(library)
            else:
                print("Invalid publication date.")
        else:
            print(f"{title_input} already exists in library.")
    elif user_input == '2':
        title_input = input("Enter the book's title: ").title()
        found = False
        for book in library:
            if book.get_title() == title_input:
                found = True
                if book.get_availability() == "Available":
                    book.borrow_book()
                    break
                else:
                    print(f"{title_input} is already borrowed.")

        if not found:
            print(f"{title_input} not found in library.")
    elif user_input == '3':
        title_input = input("Enter the book's title: ").title()
        found = False
        for book in library:
            if book.get_title() == title_input:
                found = True
                if book.get_availability() == "Borrowed":
                    book.return_book()
                    break
                else:
                    print(f"{title_input} was not borrowed.")

        if not found:
            print(f"{title_input} not found in library.")
    elif user_input == '4':
        title_input = input("Enter the book's title: ").title()
        found = False
        for book in library:
            if book.get_title() == title_input:
                found = True
                book.search_for_book()

        if not found:
            print(f"{title_input} not found in library.")
    elif user_input == '5':
        display_books(library)
    else:
        print("Invalid input. Please try again.")