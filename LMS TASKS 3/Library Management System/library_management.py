from library_utils import save_books, load_books

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availstatus = True

    def update_status(self, newstatus):
        self.availstatus = newstatus
    
    def available(self):
        return self.availstatus


class Library:
    """Holds a list of book objects and methods that can be applied to them."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} added successfully.")

    def view_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("Books in library:")
            for book in self.books:
                status = "Available" if book.available() else "Borrowed"
                print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

    def borrow_book(self, title):
        title = title.title().strip()
        for book in self.books:
            if book.title == title:
                if book.available():
                    book.update_status(False)
                    print(f"You have borrowed '{book.title}' successfully.")
                else:
                    print(f"'{book.title}' is not available for borrowing.")
                return
        print(f"'{title}' does not exist in the library.")

    def return_book(self, title):
        title = title.title().strip()
        for book in self.books:
            if book.title == title:
                if not book.available():
                    book.update_status(True)
                    print(f"You have returned '{book.title}' successfully.")
                else:
                    print(f"'{book.title}' is already available in the library.")
                return
        print(f"'{title}' does not exist in the library.")


def main():
    my_library = Library()
    my_library.books = load_books('book_data.json')

    while True:
        print()
        print("---- Library Menu -----")
        print("1. Add a New Book")
        print("2. Show All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Save & Exit")

        choice = input("Pick a number from 1-5: ").strip()
        print()

        if choice == "1":
            title = input("Enter the title of the book: ").title().strip()
            author = input("Enter the author of the book: ").title().strip()
            book = Book(title, author)
            my_library.add_book(book)
            
        elif choice == "2":
            my_library.view_books()

        elif choice == "3":
            title = input("Enter the title of the book you'd like to borrow: ")
            my_library.borrow_book(title)

        elif choice == "4":
            title = input("Enter the title of the book you'd like to return: ")
            my_library.return_book(title)

        elif choice == "5":
            ans = input("Are you sure you want to save and exit? (Y/N): ").upper().strip()
            if ans == "Y":
                save_books(my_library.books, 'book_data.json')
                print("Goodbye! Thanks for using our Library Management System.")
                break
            elif ans == "N":
                continue
            else:
                print("Invalid input. Please enter Y or N.")
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
