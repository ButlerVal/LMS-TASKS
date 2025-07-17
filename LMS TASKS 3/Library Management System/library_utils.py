import json
import os

def save_books(books, filename):
    book_list = []
    for book in books:
        book_list.append({
            "Title": book.title,
            "Author": book.author,
            "Available": book.availstatus
        })
    with open(filename, 'w') as file:
        json.dump(book_list, file, indent=4)

def load_books(filename):
    from library_management import Book
    books = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            book_list = json.load(file)
        for bks in book_list:
            book = Book(bks['Title'], bks['Author'])
            book.update_status(bks['Available'])
            books.append(book)
    else:
        print(f"{filename} does not exist. Starting with an empty library.")
    return books
