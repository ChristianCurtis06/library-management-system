# User operation module containing user operations menu and user interaction
from user_class import User
import re

users = []

# Defining a function to display all users in 'users' list with their details
def display_users(users):
    if users:
        print("User Database:")
        for user in users:
            print(f"Name: {user.get_name()}, Library ID: {user.get_id()}, Borrowed Books: {", ".join(user.get_borrowed_books())}")
    else:
        print("User database contains no users.")

# Defining a function to display user operations menu and enable user interaction
def display_user_menu():
    print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
    user_input = input("Enter your choice: ").strip()
    if user_input == '1':
        name_input = input("Enter the user's name: ").title()
        id_input = input("Enter the user's library ID: ")
        borrowed_books_input = input("Enter the user's borrowed books (separated by commas): ").title().split(", ")
        if name_input not in [user.get_name() for user in users]:
            if re.findall(r"^(\d{4})$", id_input):
                new_user = User(name_input, id_input, borrowed_books_input)
                new_user.add_user(users)
            else:
                print("Invalid library ID.")
        else:
            print(f"{name_input} already exists in user database.")
    elif user_input == '2':
        name_input = input("Enter the user's name: ").title()
        found = False
        for user in users:
            if user.get_name() == name_input:
                found = True
                user.view_user_details()

        if not found:
            print(f"{name_input} not found in user database.")
    elif user_input == '3':
        display_users(users)
    else:
        print("Invalid input. Please try again.")