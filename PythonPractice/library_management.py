
class Book:
    def __init__(self, book_id, book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if self.search_book(book.book_id) is not None:
            return False

        self.books.append(book)
        return True

    def display_books(self):
        found = False

        for book in self.books:
            if book.available:
                print("Book ID:", book.book_id)
                print("Book Name:", book.book_name)
                print("Author:", book.author)
                print("Availability: Available")
                print("--------------------")
                found = True

        if not found:
            print("No available books.")

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def borrow_book(self, book_id):
        book = self.search_book(book_id)

        if book is not None and book.available:
            book.available = False
            return True

        return False

    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book is not None and not book.available:
            book.available = True
            return True

        return False


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Available Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            book_name = input("Enter Book Name: ")
            author = input("Enter Author: ")

            book = Book(book_id, book_name, author)

            if library.add_book(book):
                print("Book added successfully!")
            else:
                print("Book ID already exists.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_id = input("Enter Book ID: ")
            book = library.search_book(book_id)

            if book is not None:
                print("Book ID:", book.book_id)
                print("Book Name:", book.book_name)
                print("Author:", book.author)
                print("Availability:", "Available" if book.available else "Borrowed")
            else:
                print("Book not found.")

        elif choice == "4":
            book_id = input("Enter Book ID: ")

            if library.borrow_book(book_id):
                print("Book borrowed successfully!")
            else:
                print("Book not found or already borrowed.")

        elif choice == "5":
            book_id = input("Enter Book ID: ")

            if library.return_book(book_id):
                print("Book returned successfully!")
            else:
                print("Book not found or already available.")

        elif choice == "6":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
