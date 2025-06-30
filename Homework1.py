class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def display_info(self):
        print(f"{self.title} by {self.author} - Copies: {self.copies_available}")

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        return False

    def return_book(self):
        self.copies_available += 1


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display_info()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, library, title):
        book = library.find_book(title)
        if book and book.borrow_book():
            self.borrowed_books.append(title)
            print(f"{self.name} borrowed '{title}'")
        else:
            print(f"'{title}' is not available.")

    def return_book(self, library, title):
        if title in self.borrowed_books:
            book = library.find_book(title)
            if book:
                book.return_book()
                self.borrowed_books.remove(title)
                print(f"{self.name} returned '{title}'")

library = Library("Central Library")
book1 = Book("Harry Potter", "Baburao", 20)
library.add_book(book1)

member = Member("Vivanshi")
library.show_books()
member.borrow(library, "Harry Potter")
member.return_book(library, "Harry Potter")