while True:
    print("""
    1. New Calculation
    2. Exit
    """)
    choice = int(input("Enter your choice:"))
    if choice == 1:
        num1 = float(input("Enter 1st number:"))
        num2 = float(input("Enter 2nd number:"))
        operator = int(input("""               
        1.+
        2.−
        3.×
        4.÷
        Select an operator:"""))

        if operator == 1:
            print(f"Result = {num1 + num2}")
        elif operator == 2:
            print(f"Result = {num1 - num2}")
        elif operator == 3:
            print(f"Result = {num1 * num2}")
        elif operator == 4:
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"Result = {num1/num2}")

        else :
            print("Wrong Input")
    elif choice == 2:
        print("Thank you for using the calculator")
        break
