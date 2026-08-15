Books ={}
def add_book():
    new_book = input("Enter the book name:")
    if new_book in Books:
        print("This book is already exists.")
    else:
        book_auth = input("Enter the author name:")
        Books[new_book]= {
            "Author":book_auth,
            "Available":True
        }
        print("")
        print("New book added successfully.")

def show_books():
    if len(Books)==0:
        print("No books available.")
    else:
        for name , data in Books.items():
            print("="*16)
            print("Book:",name)
            print("Author:",data["Author"])
            print("Available:",data["Available"])
            print()

def search_book():
    user_search_book = input("Enter the book name:")
    if user_search_book in Books:
        print("Book:",user_search_book)
        for key , value in Books[user_search_book].items():
            print(f"{key}: {value}")
            print()
    else:
        print("Book not found.")

def borrow_book():
    user_borrow_book = input("Enter the book name:")
    if user_borrow_book in Books:
        if Books[user_borrow_book]["Available"]== True:
            Books[user_borrow_book]["Available"]= False
            print("Book borrowed successfull.")
           
        else:
            print("Book is already borrowed.")
    else:
        print("Book not found.")

def return_book():
    user_return_book = input("Enter the book name:")
    if user_return_book in Books:
        if Books[user_return_book]["Available"] == False:
            Books[user_return_book]["Available"] = True
            print("Book returned successfull.")
        else:
            print("Book is already available.")   
    else:
        print("Book not found.")

def delete_book():
    user_delete_book = input("Enter the book name:")
    if user_delete_book in Books:
        warning = input("Are you sure?(Y/N):")
        if warning.lower() == "y":
            Books.pop(user_delete_book)
            print("Book delete successfull.")
        elif warning.lower() == "n":
            print("Operation cancelled.")
        else:
            print("Invalid input.")
    else:
        print("Book not found.")

def total_books():
    if len(Books) == 0:
        print("No book found.")
    else:
        print("Total book is:",len(Books)) 

def available_books():
        found = False
        for book_name , book_data in Books.items():
            if Books[book_name]["Available"] == True: 
                print(f"Available book is :{book_name}") 
                found = True
        if not found:  
                print("No book Available.")
                
while True:        
        
    print("="*8,"Library Management","="*8)
    user = int(input("""
    1. Add Book
    2. Show Books
    3. Search Book
    4. Borrow Book
    5. Return Book
    6. Delete Book
    7. Total Books
    8. Available Books
    9. Exit
    Enter your choice:"""))

    if user == 1:
        add_book()
    elif user == 2:
        show_books()
    elif user == 3:
        search_book()
    elif user == 4:
        borrow_book()
    elif user == 5:
        return_book()
    elif user == 6:
        delete_book()
    elif user == 7:
        total_books()
    elif user == 8:
        available_books()
    elif user == 9:
        print("Thanks for using our app.")
        break
    else:
        print("Invalid choice. Try again.")
