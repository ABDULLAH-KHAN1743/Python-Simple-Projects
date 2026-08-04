note = []
while True :
    options = '''
1. Add a note
2. View notes
3. Delete a note
4. Exit
'''
    print(options)
    user = input("Choose an option: ")
    if user == "1":
        x = input("Enter your note: ")
        if x == "":
            print("Note cannot be empty.")
        else:
            note.append(x)
            print("Note added successfully.")
    elif user == "2":
        print("""
1. View Previous Notes
2. View Current Notes""")
        viewnote=input("Choose an option: ")
        if viewnote =="1":
            rpn=open("test.txt","r")
            print(rpn.read())
        else:
            print(note)
    elif user == "3":
        rem = input("Enter the note you want to delete: ")
        if rem in note:
            note.remove(rem)
            print("Note deleted successfully.")
        else:
            print("Note not found.")
    elif user == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")


x = note
write = open('test.txt',"a")
write.write(str(x)+ "\n")