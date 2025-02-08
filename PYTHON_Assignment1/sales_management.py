import book_management
import customer_management

sales = []

class Transaction:
    def __init__(self, customer_name, book_title, quantity_sold):
        self.customer_name = customer_name
        self.book_title = book_title
        self.quantity_sold = quantity_sold

    def display_sale(self):
        return f"Customer: {self.customer_name}, Book: {self.book_title}, Quantity Sold: {self.quantity_sold}"

def sell_book(customer_name, book_title, quantity):
    # Check if the book exists and if there is sufficient quantity
    book = None
    for b in book_management.books:
        if b.title.lower() == book_title.lower():
            book = b
            break
    
    if not book:
        return "Error: Book not found."
    
    # Check if there are enough copies in stock
    if book.quantity < quantity:
        return f"Error: Only {book.quantity} copies available. Sale cannot be completed."
    
    # Reduce the quantity of the book
    book.quantity -= quantity
    
    # Create a sales transaction
    transaction = Transaction(customer_name, book_title, quantity)
    sales.append(transaction)
    
    return f"Sale successful! Remaining quantity: {book.quantity}"

def view_sales():
    if not sales:
        return "No sales records found."
    return [transaction.display_sale() for transaction in sales]

