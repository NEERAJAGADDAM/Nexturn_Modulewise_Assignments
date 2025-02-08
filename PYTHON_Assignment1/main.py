import book_management
import customer_management
import sales_management

def display_menu():
    print("Welcome to BookMart!")
    print("1. Book Management")
    print("2. Customer Management")
    print("3. Sales Management")
    print("4. Exit")

def validate_positive_number(input_value, input_type="number"):
    try:
        value = float(input_value)
        if value <= 0:
            print(f"Invalid input! {input_type.capitalize()} must be a positive number.")
            return None
        return value
    except ValueError:
        print(f"Invalid input! Please enter a valid {input_type}.")
        return None

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nBook Management")
            action = input("1. Add Book\n2. View Books\n3. Search Book\n4. Update Book\n5. Delete Book\nEnter your choice: ")
            if action == '1':
                title = input("Title: ")
                author = input("Author: ")
                price = validate_positive_number(input("Price: "), "price")
                if price is None:
                    continue
                quantity = validate_positive_number(input("Quantity: "), "quantity")
                if quantity is None:
                    continue
                print(book_management.add_book(title, author, price, quantity))
            elif action == '2':
                print("\n".join(book_management.view_books()))
            elif action == '3':
                title = input("Enter title to search: ")
                author = input("Enter author to search: ")
                print("\n".join(book_management.search_book(title=title, author=author)))
            elif action == '4':
                title = input("Enter title of the book to update: ")
                new_title = input("New Title (leave blank to keep current): ")
                new_author = input("New Author (leave blank to keep current): ")
                new_price = validate_positive_number(input("New Price (leave blank to keep current): "), "price")
                new_quantity = validate_positive_number(input("New Quantity (leave blank to keep current): "), "quantity")
                print(book_management.update_book(title, new_title, new_author, new_price, new_quantity))
            elif action == '5':
                title = input("Enter title of the book to delete: ")
                print(book_management.delete_book(title))
        elif choice == '2':
            print("\nCustomer Management")
            action = input("1. Add Customer\n2. View Customers\nEnter your choice: ")
            if action == '1':
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                print(customer_management.add_customer(name, email, phone))
            elif action == '2':
                print("\n".join(customer_management.view_customers()))
        elif choice == '3':
            print("\nSales Management")
            action = input("1. Sell Book\n2. View Sales Records\nEnter your choice: ")
            if action == '1':
                customer_name = input("Customer Name: ")
                book_title = input("Book Title: ")
                quantity = validate_positive_number(input("Quantity: "), "quantity")
                if quantity is None:
                    continue
                print(sales_management.sell_book(customer_name, book_title, quantity))
            elif action == '2':
                print("\n".join(sales_management.view_sales()))
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

