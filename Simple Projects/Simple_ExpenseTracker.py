expenses = []
def add_expense():
    user_name = input("Enter the expense name:")
    user_amount = int(input("Enter the amount:"))
    user_category = input("Enter the category name:")
    expense ={
        "Name":user_name,
        "Amount":user_amount,
        "Category":user_category
    }
    expenses.append(expense)
    print("Expense added successfully.")

def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("="*5, "All Expenses", "="*5)
        for item in expenses:
            print("Name:",item["Name"])
            print("Amount:",item["Amount"])
            print("Category:",item["Category"])
            print()

def total_expense():
     
    if len(expenses) == 0:
            print("No expenses found.")
    else:
        total = 0
        for item in expenses:
            total = total + item["Amount"]
        print(f"Total Expense: {total}")     

def search_expense():
    if len(expenses) == 0:
        print("No expense found.")
    else:
        user_search = input("Enter expense name:")
        found = False
        for item in expenses:
            if item["Name"] == user_search:
                found = True
                print("="*5,"Search Expense","="*5 )
                print("Name:", user_search)
                print("Amount:", item["Amount"])
                print("Category:", item["Category"])
                
        if not found:
            print()
            print("Expense not found.")

def delete_expense():
    for num , item in enumerate(expenses, start = 1):
        print(num, "Name:",item["Name"])
        print("Amount:",item["Amount"])
        print("Category:",item["Category"])
        print()
        
    if len(expenses) == 0:
            print("No expense found.")
    else:
        user_delete = int(input("Enter expense number to delete:"))
        if user_delete < 1 or user_delete > len(expenses):
            print("Invalid expense number.")
        else:
            expenses.pop(user_delete-1)
            print("Expense delete successfull.")

def total_category():
    category_total = {}
    for item in expenses:
        category = item["Category"]
        amount = item["Amount"]
        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount
    for category , total in category_total.items():
        print(category, ":", total) 

while True:
    user = int(input("""
===== Expense Tracker =====

1. Add Expense
2. Show Expenses
3. Total Expense
4. Search Expense
5. Delete Expense
6. Category Total
7. Exit
Enter your choice:"""))
    if user == 1:
        add_expense()
    elif user == 2:
        show_expenses()
    elif user == 3:
        total_expense()
    elif user == 4:
        search_expense()
    elif user == 5:
        delete_expense()
    elif user == 6:
        total_category()
    elif user == 7:
        print("Thanks for using our app.")
        break
    else:
        print("Invalid choice.")