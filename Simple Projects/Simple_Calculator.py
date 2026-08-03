num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
operator = int(input("""               
1.+
2.−
3.×
4.÷
Select an operator:"""))

if operator == 1:
    print(num1 + num2)
elif operator == 2:
    print(num1 - num2)
elif operator == 3:
    print(num1 * num2)
elif operator == 4:
    print(num1/num2)

else :
    print("Wrong Input")