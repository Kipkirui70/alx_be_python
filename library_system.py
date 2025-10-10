# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}MB"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # list to hold all book objects

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Print all books in the library"""
        if not self.books:
            print("The library is empty.")
        else:
            print("\nBooks in the Library:")
            for book in self.books:
                print(f" - {book}")
