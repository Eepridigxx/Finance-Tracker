import pickle

def display_expense_month():
    try:
        filehandler = open("expenses.dat", "rb")
        all_expenses_list = pickle.load(filehandler)
        if all_expenses_list == []:
            print("       ⚠️ Sorry there are currently no expenses yet!")
        else:
            filehandler2 = open("budget.dat" , "rb")
            all_budget_list = pickle.load(filehandler2)
            all_months_list = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
            month_name = input("       Enter the month name : ").strip().capitalize()
            if month_name not in all_months_list:
                print("     ⚠️ Sorry invalid month name!")
            else:    
                if month_name == "January":
                    month_number = '01'
                elif month_name == "February":
                    month_number = '02'
                elif month_name == "March":
                    month_number = '03'
                elif month_name == "April":
                    month_number = '04'
                elif month_name == "May":
                    month_number = '05'
                elif month_name == "June":
                    month_number = '06'
                elif month_name == "July":
                    month_number = '07'
                elif month_name == "August":
                    month_number = '08'
                elif month_name == "September":
                    month_number = '09'
                elif month_name == "October":
                    month_number = '10'
                elif month_name == "November":
                    month_number = '11'
                else:
                    month_number = '12'
                #roaming through the dictionaries in the list
                total_expenses = 0
                money_spent = 0
                for expense_dic in all_expenses_list:
                    if expense_dic["Date"].split('-')[1] == month_number:
                        print("      📆  Date ➜ " , expense_dic["Date"])
                        print("      💰  Amount ➜ " , expense_dic["Amount"])
                        print("      🏡  Place ➜ " , expense_dic["Place"])
                        print("      🗒️  Description ➜ " , expense_dic["Description"])
                        print("      ⌨️  Expense Id ➜ " , expense_dic["Expense Id"])
                        print()
                        total_expenses = total_expenses + 1
                        money_spent = money_spent + expense_dic["Amount"]
                    else:
                        pass
                if total_expenses == 0:
                    print("      🤓 You have not added any expenses for the month of " , month_name)
                else:
                    print(f"     🤓  There have been {total_expenses} expenses made in the month of {month_name}!")
                    print(f"     📣  Total money spent this month is ₹ {money_spent}")
                for budder in all_budget_list:
                    if budder["Name"] == month_name:
                        budget_monther = budder["Budget"]
                        if money_spent > budget_monther:
                            print(f"       🥶 You have exceeded the monthly budget for the month of {month_name}!")
                        else:
                            print(f"       😎 You are safe as  expenses for the month of {month_name} have not crossed the budget! ")
                        break
    except FileNotFoundError:
        print("      😔 Sorry there are currenty no expenses yet!")
    except Exception as e:
        print("      😔 Sorry there are currenty no expenses yet!")
        print(e)

