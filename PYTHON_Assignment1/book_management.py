class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def display_book(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Quantity: {self.quantity}"

    def update_book(self, title=None, author=None, price=None, quantity=None):
        if title: self.title = title
        if author: self.author = author
        if price: self.price = price
        if quantity: self.quantity = quantity
        return "Book updated successfully!"

# Functions to add a book, view all books, search for a book, delete a book, and update a book
books = []

def add_book(title, author, price, quantity):
    book = Book(title, author, price, quantity)
    books.append(book)
    return "Book added successfully!"

def view_books():
    return [book.display_book() for book in books]

def search_book(title=None, author=None):
    result = []
    for book in books:
        if title and title.lower() in book.title.lower():
            result.append(book.display_book())
        elif author and author.lower() in book.author.lower():
            result.append(book.display_book())
    return result if result else "No books found."

def delete_book(title):
    global books
    books = [book for book in books if book.title.lower() != title.lower()]
    return f"Book titled '{title}' has been deleted successfully." if books else "No book found with that title."

def update_book(title, new_title=None, new_author=None, new_price=None, new_quantity=None):
    for book in books:
        if book.title.lower() == title.lower():
            return book.update_book(new_title, new_author, new_price, new_quantity)
    return "Book not found."

