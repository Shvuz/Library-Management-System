class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            title, author, _, _ = book.split(',')
            print(f"Title: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter first release year: ")
        pages = input("Enter number of pages: ")
        self.file.write(f"{title},{author},{year},{pages}\n")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        for i, book in enumerate(books):
            title, _, _, _ = book.split(',')
            if title == title_to_remove:
                del books[i]
                break
        self.file.truncate(0)
        self.file.writelines(books)

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice: ")
    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    else:
        print("Invalid choice. Please try again.")
