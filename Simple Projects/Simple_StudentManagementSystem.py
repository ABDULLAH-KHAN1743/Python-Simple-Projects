students={}
def add_students():
    name = input("Enter student name:")
    if name in students:
        print("Student already exists.")
    else:
        age = int(input("Enter student age:"))
        roll = int(input("Enter student roll:"))
        students[name]={
            "Age":age,
            "Roll":roll
        }
        print("")
        print("Student added successfully.")

def show_students():
    if len(students)==0:
        print("No student found.")
    else:
        for name , data in students.items():
            print("=============================")
            print("Name:",name)
            print("Age:",data["Age"])
            print("Roll:",data["Roll"])

def search_students():
        search = input("Enter the student name:")
        if search in students:
             
            print("=============================")
            print("Name:",search)
            for key,value in students[search].items():
                print(f"{key}: {value}")
            print("")
        else:
             print("Student not found.")

def update_students():
    update = input("Enter the student name:")
    if update in students:
        update_age = int(input("Enter student age:"))
        update_roll = int(input("Enter student roll:"))
        students[update]["Age"]= update_age
        students[update]["Roll"]= update_roll
        print("")
        print("Student update successfully.")
    else:
        print("Student not found.")

def delete_student():
    delete = input("Enter the student name:")
    if delete in students:
        students.pop(delete)
        print("Student delete successfully.")
    else:
        print("Student not found.")

def total_students():
    print("Total students:",len(students))

def clear_all_students():
    confirm = input("Are you sure? (y/n):")
    if confirm.lower() == "y":
        students.clear()
        print("All data clear successfully.")
    else:
        print("Operation cancelled.")

while True:

    user = int(input("""

    ===== Student Management =====

    1. Add Student
    2. Show Students
    3. Search Student
    4. Update Student
    5. Delete Student
    6. Total Students
    7. Clear All Students
    8. Exit

    Enter choice:"""))

    if user == 1:
        add_students()
    elif user == 2:
        show_students()
    elif user == 3:
        search_students()
    elif user == 4:
        update_students()
    elif user == 5:
        delete_student()
    elif user == 6:
        total_students()
    elif user == 7:
        clear_all_students()
    elif user == 8:
        print("Thanks for using our app.")
        break
    else:
        print("Invalid choice.")
