accounts = {}

def create_account():
    user_name = input("Enter your name:")
    if user_name in accounts:
         print("Account already exists.")
    else:
        user_pass = input("Enter your password:")
        try:
          user_balance = int(input("Enter your balance:"))
          if user_balance >= 0:
               accounts[user_name] = {
                         "Password" : user_pass,
                         "Balance" : user_balance,
                         "History":[]
               }
               print()
               print("Account created successfully.")
          else:
               print("Invalid balance.")
        except ValueError:
             print("Balance must be a number.")

def show_account():
    name = input("Enter your name:")
    passw = input("Enter your password:")
    if name in accounts:
        if passw == accounts[name]["Password"]:
                print()
                print("="*20)
                print("Name:",name )
                print("Balance",accounts[name]["Balance"])
        else:
                print("Wrong password.")
    else:
         print("Account not found.")

def deposit_money():
    deposit_name = input("Enter your name:")
    deposit_pass = input("Enter your password:")
    try:  
     deposit_amount = int(input("Enter amount to deposit:"))
     if deposit_name in accounts:
          if deposit_pass == accounts[deposit_name]["Password"]:
               if deposit_amount > 0:
                         accounts[deposit_name]["Balance"] += deposit_amount
                         accounts[deposit_name]["History"].append(
                              f"Deposit:{deposit_amount}"
                         )
                         print("Money deposited successfully.")
                         print("New Balance:", accounts[deposit_name]["Balance"])

               else:
                         print("Invalid amount.")
          else:
                    print("Wrong password.")
     else:
               print("Account not found.")
    except ValueError:
         print("Amount must be a number.")

def withdraw_money():
     withdraw_name = input("Enter your name:")
     withdraw_pass = input("Enter your password:")
     try:
          withdraw_amount = int(input("Enter amount to withdraw:"))
          if withdraw_name in accounts:
               if withdraw_pass == accounts[withdraw_name]["Password"]:
                    if withdraw_amount > 0 and withdraw_amount <= accounts[withdraw_name]["Balance"]:
                         accounts[withdraw_name]["Balance"] -= withdraw_amount
                         accounts[withdraw_name]["History"].append(
                              f"Withdraw:{withdraw_amount}"
                         )
                         print("Withdraw successful.")
                    else:
                         print("Wrong amount. Balance not found.")
               else:
                    print("Wrong password.")
          else:
               print("User not found.")
     except ValueError:
          print("Amount must be a number.")

def transfer_money():
     transfer_user = input("Enter your name:")
     transfer_pass = input("Enter your password:")
     try:
          transfer_amount = int(input("Enter transfer amount:"))
          receiver = input("Enter receiver name:")
          if transfer_user == receiver:
               print("You cannot transfer money to yourself.")
          else:
           if transfer_user in accounts:
                    if transfer_pass == accounts[transfer_user]["Password"]:
                         if transfer_amount > 0 and transfer_amount <= accounts[transfer_user]["Balance"]:
                              if receiver in accounts:
                                   warning = input("Are you sure? Y/N:")
                                   if warning.lower() == "y":
                                        accounts[transfer_user]["Balance"] -= transfer_amount
                                        accounts[receiver]['Balance'] += transfer_amount
                                        accounts[transfer_user]["History"].append(
                                             f"Transferred {transfer_amount} to {receiver}"
                                        )
                                        accounts[receiver]["History"].append(
                                             f"Received {transfer_amount} from {transfer_user}"
                                        )
                                        print("Operation successful.")
                                        print(f"Your current balance is: {accounts[transfer_user]['Balance']}")
                                   else:
                                        print("Operation cancelled.")
                              else:
                                   print("Receiver not found.")
                         else:
                              print("Wrong amount.")
                    else:
                         print("Wrong password.")
           else:
               print("User not found.")
     except ValueError:
          print("Amount must be a number.")

def transaction_history():
     history_user = input("Enter your name:")
     history_pass = input("Enter your password:")
     if history_user in accounts:
          if history_pass == accounts[history_user]["Password"]:
               history = accounts[history_user]["History"]
               if len(history) == 0:
                    print("No transaction found.")
               else:
                    print("="*15)
                    print("Transaction History")
                    print("="*15)
                    for item in history:
                         print("-", item)
          else:
               print("Wrong password.") 
     else:
          print("Account not found.")

while True:
    print("""
    ====== Bank Account Management System ======
    1. Create Account
    2. Show Account
    3. Deposit Money
    4. Withdraw Money
    5. Transfer Money
    6. Transaction History
    7. Exit
    """)
    try:
         user = int(input("Enter your choice:"))
         if user == 1:
               create_account()
         elif user == 2:
               show_account()
         elif user == 3:
               deposit_money()
         elif user == 4:
               withdraw_money()
         elif user == 5:
               transfer_money()
         elif user == 6:
               transaction_history()
         elif user == 7:
               print("Thank you for using Bank Account Management System.")
               break
         else:
              print("Invalid choice.")
    except ValueError:
         print("Please enter a number.")