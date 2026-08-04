items = []
num = 1
while True:
    options = int(input("""
    1. Add Items
    2. Show Items
    3. Delet Items
    4. Exit

    Enter your choice:"""))
    if options == 1:
        item = input("Enter your item name:")
        items.append(item)
    elif options == 2:
        if len(items)==0:
            print("There is no item in the list.")
        else:
            for num,i in enumerate(items,start=1):
                print(num, i)
                
    elif options == 3:
         for num,i in enumerate(items,start=1):
            print(num, i)
            
         rem = int(input("Which item you want to remove:"))
         rem -= 1
         if 0 <= rem < len(items):
                
                items.pop(rem)
         else:
                print("Item not found.")
    elif options == 4:
        print("Thanks for using our app.")
        break
    else:
        print("Invalid option. Try again.")