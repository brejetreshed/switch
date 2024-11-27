#Implementing as list:
#Pros: Easy to implement and understand. Easy to maintain.
#Cons: Linear search O(n).



class Book:
    def __init__(self, title, authors, genre, publication_year, isbn=None):
        self.title = title
        self.authors = authors
        self.genre = genre
        self.publication_year = publication_year
        self.isbn = isbn

    def __str__(self):
        return (f"Title: {self.title}, Authors: {', '.join(self.authors)}, "
                f"Genre: {self.genre}, Year: {self.publication_year}, "
                f"ISBN: {self.isbn or 'N/A'}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, authors, genre, publication_year, isbn=None):
        book = Book(title, authors, genre, publication_year, isbn)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print(f"Books matching title '{title}':")
            for book in results:
                print(book)
        else:
            print(f"No books found with title '{title}'.")

    def search_by_author(self, author):
        results = [book for book in self.books if any(author.lower() in a.lower() for a in book.authors)]
        if results:
            print(f"Books by author '{author}':")
            for book in results:
                print(book)
        else:
            print(f"No books found by author '{author}'.")

    def display_books(self):
        if self.books:
            print("Library Catalog:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")


