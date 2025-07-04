
library = []

def add_book():
    book = input("Enter book name to add: ")
    library.append(book)
    print(f"'{book}' has been added to the library.\n")

def view_books():
    if library:
        print("Books available in the library:")
        for i, book in enumerate(library, 1):
            print(f"{i}. {book}")
    else:
        print("Library is empty.")
    print()

def issue_book():
    book = input("Enter book name to issue: ")
    if book in library:
        library.remove(book)
        print(f"'{book}' has been issued.\n")
    else:
        print(f"'{book}' is not available in the library.\n")

def return_book():
    book = input("Enter book name to return: ")
    library.append(book)
    print(f"'{book}' has been returned to the library.\n")

def delete_book():
    book = input("Enter book name to delete: ")
    if book in library:
        library.remove(book)
        print(f"'{book}' has been deleted from the library.\n")
    else:
        print(f"'{book}' not found in the library.\n")

def menu():
    while True:
        print("=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("Exiting the LMS. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the menu
menu()
