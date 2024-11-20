# Class module containing 'Book' class with its object methods
class Book:
    def __init__(self, title, author, genre, publication):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication = publication
        self.__availability = "Available"

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre
    
    def get_publication(self):
        return self.__publication
    
    def get_availability(self):
        return self.__availability

    def add_book(self, library):
        library.append(self)
        print(f"{self.__title} added to library.")

    def borrow_book(self):
        self.__availability = "Borrowed"
        print(f"{self.__title} borrowed from library.")

    def return_book(self):
        self.__availability = "Available"
        print(f"{self.__title} returned to library.")

    def search_for_book(self):
        print(f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publication Date: {self.__publication}, Availability Status: {self.__availability}")