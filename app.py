from utils import database

USER_CHOICE = """
Enter:
-> 'a' to add a new book
-> 'l' to list all the books
-> 'm' to mark all books as read
-> 's' to search a book
-> 'd' to delete a book
-> 'q' to quit
Your Choice:
"""


# Create the menu function
def menu():
    user_input = input(USER_CHOICE)
    # deal-with the users input choice
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_new_book()
        elif user_input == "l":
            list_books()
        elif user_input == 'r':
            prompt_mark_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Invalid choice, please try again")
        user_input = input(USER_CHOICE)


# Create a function to prompt the user to add a new book(name, author)
def prompt_add_new_book():
    name = input("Enter The Name Of The New Book: ")
    author = input("Enter The Author Of The New Book: ")
    database.add_book(name, author)


# Create a function to show all the books
def list_books():
    books = database.get_all_books()
    for book in books:
        read = "Yes" if book['read'] == "1" else "No"
        print(f"{book['name']}, written by {book['author']}, Read Status: {read}")


# Create a function to mark a book as read
def prompt_mark_book():
    name = input("Enter the name of the book you've finished reading: ")
    database.mark_book_as_read(name)


# Create a function to delete books
def prompt_delete_book():
    name = input("Enter the name of the book you would like to delete: ")
    database.delete_book(name)


menu()
