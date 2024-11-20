# Main module containing main menu, user interaction, error handling
import book_operations
import user_operations
import author_operations

def main():
    print("Library Management System")
    while True:
        try:
            print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
            user_input = input("Enter your choice: ").strip()
            if user_input == '1':
                book_operations.display_book_menu()
            elif user_input == '2':
                user_operations.display_user_menu()
            elif user_input == '3':
                author_operations.display_author_menu()
            elif user_input == '4':
                print("Quitting the system...")
                break
            else:
                print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()