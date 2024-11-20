# Class module containing 'Author' class with its object methods
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography

    def add_author(self, authors):
        authors.append(self)
        print(f"{self.__name} added to author database.")

    def view_author_details(self):
        print(f"Name: {self.__name}, Biography: {self.__biography}")