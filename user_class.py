# Class module containing 'User' class with its object methods
class User:
    def __init__(self, name, id, borrowed_books):
        self.__name = name
        self.__id = id
        self.__borrowed_books = borrowed_books

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_borrowed_books(self):
        return self.__borrowed_books
    
    def add_user(self, users):
        users.append(self)
        print(f"{self.__name} added to user database.")

    def view_user_details(self):
        print(f"Name: {self.__name}, Library ID: {self.__id}, Borrowed Books: {", ".join(self.__borrowed_books)}")