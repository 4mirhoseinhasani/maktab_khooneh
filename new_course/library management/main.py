from mylibrary import Library
from tabulate import tabulate


def show_menu():
    menu = [
        ["1", "show books"],
        ["2", "add book"],
        ["3", "remove book"],
        ["4", "search book"],
        ["5", "exit"]
    ]

    print(tabulate(menu, headers=["Option", "Description"], tablefmt="fancy_grid"))

if __name__ == '__main__':
    library = Library()

    while True:
        show_menu()
        choice = input("select an option: ")
        
        if choice == '1':
            library.show_books()

        if choice == '2':
            title = input("your book title: ")
            author = input("Author of the book: ")
            library.add_book(title, author="unknown")

        if choice == '3':
            title = input("Enter book title for remove: ")
            library.remove_book(title)

        if choice == '4':
            title = input("Enter book title to search: ")
            library.search_book(title)

        
        if choice == '5':
            break