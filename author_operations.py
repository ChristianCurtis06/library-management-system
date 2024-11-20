# Author operation module containing author operations menu and user interaction
from author_class import Author

authors = []

# Defining a function to display all authors in 'authors' list with their details
def display_authors(authors):
    if authors:
        print("Author Database:")
        for author in authors:
            print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")
    else:
        print("Author database contains no authors.")

# Defining a function to display author operations menu and enable user interaction
def display_author_menu():
    print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
    user_input = input("Enter your choice: ").strip()
    if user_input == '1':
        name_input = input("Enter the author's name: ").title()
        biography_input = input("Enter the author's biography: ").capitalize()
        if name_input not in [author.get_name() for author in authors]:
            new_author = Author(name_input, biography_input)
            new_author.add_author(authors)
        else:
            print(f"{name_input} already exists in author database.")
    elif user_input == '2':
        name_input = input("Enter the author's name: ").title()
        found = False
        for author in authors:
            if author.get_name() == name_input:
                found = True
                author.view_user_details()

        if not found:
            print(f"{name_input} not found in user database.")
    elif user_input == '3':
        display_authors(authors)
    else:
        print("Invalid input. Please try again.")