#-------------------------------------------
# Program Name: Library Management System
# Author: Jonathan Canola
# Date: 03/22/2026
#-------------------------------------------
# Pseudocode:
# 1. DISPLAY main_menu create empty book_inventory
# 2. INPUT main_menu selection 1-5
# 3. IF userINPUT 1 add_book 
# 4. INPUT title and author
# 5. INPUT number of copies
# 6. add book to book_inventory if copies > 0
# 7. ELSE DISPLAY error
# 8. ELIF userINPUT 2 borrow
# 9. INPUT title for book_search
# 10. IF book in book_inventory then book copies updated and borrowed
# 11. ELSE DISPLAY no copies available
# 12. ELIF userINPUT 3 return_book
# 13. INPUT title for book_checked
# 14. IF book_checked title in book_inventory book is returned copies updated
# 15. ElSE DISPLAY error
# 16. ELIF userINPUT 4 display_library
# 17. DISPLAY empty message is inventory is empty
# 18. ELSE DISPLAY current library inventory
# 19. ELIF userINPUT 5 exit program
# 20. ELSE DISPLAY error message
#-------------------------------------------
# Program Inputs: Book title, author, and copies
# Program Outputs: Displays inventory, success message when checked out or returned
#-------------------------------------------

# Function to add book to inventory
def add_book(book_inventory):
    # Asks user for title and author
    title = input("Book Title: ")
    author = input("Author: ")

    try:
        # Asks user for copies quanity 
        copies = int(input("Number of copies: "))
        # Validates input is greater than 0
        if copies > 0:
            book = {"title": title, "author": author, "copies": copies}
            # Adds book to inventory
            book_inventory.append(book)
            print("-" * 40)
            # Lets user know book was added
            print("Book added.")
            print("-" * 40)
        else:
            # Error message if quanity isnt enough
            print("Not enough copies.")

    except ValueError:
        # Error message if number was not enter for copies
        print("Error: Enter whole number for copies.")

# Function to borrow a book
def borrow(book_inventory):
   # Asks user for book title 
   book_search = input("Enter book title: ")
   title_found = False

   for book in book_inventory:
       # Validates book title in inventory
       if book['title'].lower() == book_search.lower():
           title_found = True
           # Validates enough copies 
           if book['copies'] > 0:
               # Subtracts a copy 
               book['copies'] -= 1
               print("-" * 40)
               # Displays success message that book was checked out
               print(f"You checked out {book['title']}.")
               print("-" * 40)
           else:
               # Error message if none available 
               print("Sorry no copies are available.")
           break
    # Error message if title isnt in inventory
   if not title_found:
       print("-" * 40)
       print(f"{book['title']} not in inventory.")
       print("-" * 40)

# Function to return a book
def return_book(book_inventory):
    # Asks user for book title 
    book_checked = input("Enter book title: ")
    book_found = False
    for book in book_inventory:
        # Validates book title in inventory
        if book['title'].lower() == book_checked.lower():
            # Adds a copy
            book['copies'] += 1
            print("-" * 40)
            # Success message that book is returned
            print(f"{book['title']} returned successful. Inventory updated.")
            print("-" * 40)
            book_found = True
            break
    # Error message if book is not in inventory 
    if not book_found:   
        print("-" * 40) 
        print(f"{book['title']} not part of inventory.")
        print("-" * 40)

# Function to display inventory
def display_library(book_inventory):
    # Error message if inventory is empty
    if not book_inventory:
        print("Book inventory is empty.")
    else:
        # Displays currenty library inventory
        print("-" * 40)
        print("\n Current Book Inventory ")
        print("-" * 40)

        for book in book_inventory:
            print(f"Title: {book['title']} | Author: {book['author']} | Coppies: {book['copies']}")

# Main menu Function
def main_menu():
    # Empty book dictionary
    book_inventory = []

    while True:
        # Displays menu options 
        print("-" * 40)
        print(" Library Management System ")
        print("-" * 40)
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Inventory")
        print("5. Exit")

        # Asks user for menu selection
        user_choice = input("Please make your selection: ")
        # Loops through to correct function based on user input 
        if user_choice in ['1', '2', '3', '4', '5']:
            # Jumps to add book function
            if user_choice == '1':
                add_book(book_inventory)
            # Jumps to borrow function
            elif user_choice == '2':
                borrow(book_inventory)
            # Jumps to return function    
            elif user_choice == '3':
                return_book(book_inventory)
            # Jumps to display inventory function
            elif user_choice == '4':
                display_library(book_inventory)
            # Exits program
            elif user_choice == '5':
                print("Exiting program. Goodbye.")
                break
        else:
            # Error message if user enter invalid selection
            print("Invalid selction. Please try again.")
# Invokes main menu function
main_menu()