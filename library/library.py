# Create a Book class, that has an author, a title and a release year
# Create a constructor for setting those values
# Book should be represented as string in this format:
# Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
# Create a BookShelf class that has a list of books in it
# We should be able to add and remove books.
# We should be able to query the favourite author (who has written the most books in the shelf)
# We should be able to query the earliest published books.
# We should be able to query the latest published books.
# Bookself should have a method whitch give us information about the number of books, the earliest and the latest released books, and the favourite author

import random

class Book():

    def __init__(self, author, title, release_year):
        self.author = author
        self.title = title
        self.release_year = release_year

class Bookshelf(Book):

    def __init__(self):
        super().__init__()
            self.empty_bookshelf = []

    def add_books(self, books):
        self.empty_bookshelf.append(books)

    def remove_books(self, books):
        self.empty_bookshelf.remove(books)

    def query_author(self):
        for query in empty_bookshelf:
            if query in empty_bookshelf:
                empty_bookshelf[query] += 1
            else:
                empty_bookshelf[query] = 1


my_shelf = BookShelf()
print(my_shelf.books())
# Should print out:
# You have no books here.

my_shelf.put("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
my_shelf.put("Douglas Adams", "Mostly Harmless", 1992)
my_shelf.put("Frank Herbert", "Dune", 1965)
my_shelf.put("Frank Herbert", "The Dragon in the Sea", 1957)
my_shelf.remove("The Dragon in the Sea")

print(my_shelf.books())
# Should print out:
# You have 3 books.
# Earliest released: Frank Herbert : Dune (1965)
# Latest released: Douglas Adams : Mostly Harmless (1992)
# Favourite author: Douglas Adams
