#importing the func1 and other files  that contains functions
import func1 , func2 , func3 , func4

#creating the menu for the expense/finance tracker program 
print('''\n\t\t\t💵  COIN PILOT - EXPENSE/FINANCE TRACKER  💵
  
            Give the corresponding number as an input to  perform the below operations ⬇️\n
            \t  1.🎯 To set new monthly  budgets.
            \t  2.🛒 To append a  monthly  budget to already existing list.
            \t  3.📹 To display pre existing  monthly budget records. 
            \t  4.🖊️ Update budget history.
            \t  5.🗑️ To delete a monthly budget.
            \t  6.🪠 To clear all budget history.
            \t  7.➕ To add new series of expenses.
            \t  8.➕ To add an expense to already existing list of expenses.
            \t  9.🎥 To display all the expenses added.
            \t  10.📹 To display an expense status by month.
            \t  11.🗑️ To delete an expense.
            \t  12.🧹 To clear the expense history. 
            \t  13.🔍 To search an expense by place.  
            \t  14.📗To know the purpose of the program
            \t  15.↩️ To exit the program.

◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽◽
''')


#now taking user inputs using an infinitely running while loop
while True:
        try:
            user_input = int(input("\n\n📢🔴  Enter the action you wanna perform (1-14) ➜  "))
            if user_input  == 1:
                func1.set_budget()
            elif user_input == 2:
                func1.append_budget()
            elif user_input == 3:
                func1.display_budget()
            elif user_input == 4:
                func1.update_budget()
            elif user_input == 5:
                func1.delete_budget_month()
            elif user_input == 6:
                func1.clear_budget_history()
            elif user_input == 7:
                func2.add_expense()
            elif user_input == 8:
                func2.append_expense()
            elif user_input == 9:
                func3.display_expense()
            elif user_input == 10:
                func4.display_expense_month()
            elif user_input == 11:
                func3.delete_expense()
            elif user_input == 12:
                func3.clear_all_expenses()
            elif user_input == 13:
                func3.search_by_place()
            elif user_input == 14:
                func4.expense_status()
            elif user_input == 15:
                func3.purpose_program()
            elif user_input == 16:
                print("\n       😊 Thanks for using our program . Come back soon!")
                break
            else:
                print("\n\t❌  Sorry invalid input , please provide input from (1-14)")
        except ValueError:
            print("      🙊 You seem to have given an invalid value , provide numbers from (1-14)")