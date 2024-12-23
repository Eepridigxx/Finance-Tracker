#importing the pickle module
import pickle

def add_expense():
    filehandler = open("expenses.dat", "wb")
    filehandler2 = open("budget.dat", "rb")

    # Asking for total expenses from the user
    total_expenses = int(input("       Enter the total number of expenses 💸 ➤ "))
    if total_expenses <= 0:
        print("\n     🙏 Please provide a valid value!")
    else:
        all_budget_list = pickle.load(filehandler2)
        if all_budget_list == []:
            print("\n       ⚠️ You have not added any budgets yet. Please press 1 to set budgets!")
        else:
            all_months_list = []
            all_month_31_days = ['01', '03', '05', '07', '08', '10', '12']
            all_month_30_days = ['04', '06', '09', '11']
            all_expenses_list = []

            for dic in all_budget_list:
                all_months_list.append(dic["Month Number"])

            new_budget_list = []

            expense_added = 0
            for ner in range(total_expenses):
                expense_added = expense_added + 1
                while True:
                    # Collecting expense details
                    expense_date = input("      Enter the expense date (dd-mm-yyyy) 📅 ➤   ")
                    try:
                        day, month, year = expense_date.split('-')
                    except ValueError:
                        print("\n      ☹️  Sorry, you have entered an invalid date!")
                        continue

                    expense_amt = float(input("      Enter the amount 💵 ➤ "))
                    if expense_amt <= 0:
                        print("\n     ☹️  Sorry, you have entered an invalid amount!")
                        continue

                    if month not in all_months_list:
                        print("\n     ☹️  Sorry, you have not set a budget for this month!")
                        break

                    # Validate the day of the month
                    if (month in all_month_31_days and (1 <= int(day) <= 31)) or \
                       (month in all_month_30_days and (1 <= int(day) <= 30)) or \
                       (month == '02' and (1 <= int(day) <= 29)):  # Basic check for February
                        diction_expenser = {}
                        diction_expenser["Date"] = expense_date
                        diction_expenser["Amount"] = expense_amt
                        diction_expenser["Place"] = input("      Enter the place of the expense 🏕️  ➤  ").strip().capitalize()
                        diction_expenser["Description"] = input("      Enter a brief description ✍️  ➤  ")

                        for dico in all_budget_list:
                            if dico["Month Number"] == month:
                                budget_month = dico["Budget"]
                                remaining_budget = dico["Remaining_Budget"]

                                if expense_amt > remaining_budget:
                                    print("      🥶    Your purchase exceeds the monthly budget!")
                                else:
                                    print("      😊    Your purchase lies within the monthly budget!\n")
                                    dico["Remaining_Budget"] -= expense_amt
                                
                                # Update the new budget list with the modified budget
                                new_budget_list.append(dico)
                            else:
                                new_budget_list.append(dico)

                        diction_expenser["Expense Id"] = "EXPENSO" + str(expense_added)
                        all_expenses_list.append(diction_expenser)
                        print("      ✅  Expense has been added!")
                        break
                    else:
                        print("      ☹️  Invalid day for the selected month!")
                        continue

            # Save updated budgets and expenses
            filehandler3 = open("budget.dat", "wb")
            pickle.dump(new_budget_list, filehandler3)
            pickle.dump(all_expenses_list, filehandler)
            if all_expenses_list == []:
                print("      ✅ No expenses were added!")
            else:
                print(f"      ✅ {len(all_expenses_list)} expenses have been added successfully!")
            filehandler3.close()

    filehandler.close()
    filehandler2.close()

    

def append_expense():
    try:
        filehandler1 = open("expenses.dat", "rb")
        all_expenses_list = pickle.load(filehandler1)
        
        if all_expenses_list == []:
            print("      ☹️ Sorry, there are currently no pre-existing expenses!")
        else:
            filehandler2 = open("budget.dat", "rb")
            all_budget_list = pickle.load(filehandler2)
            all_months_budget = []

            for dic in all_budget_list:
                all_months_budget.append(dic["Month Number"])

            # Asking for expense details from the user
            while True:
                total_expenses = len(all_expenses_list)
                expense_date = input("       Enter the expense date (dd-mm-yyyy) 📅  ➤ ")
                expense_amt = float(input("      Enter the amount 💵  ➤ "))
                expense_place = input("       Enter the place of the expense 🏕️  ➤  ").strip().capitalize()
                expense_desc = input("       Enter a brief description ✍️ ➤ ")
                all_month_31_days = ['01', '03', '05', '07', '08', '10', '12']
                all_month_30_days = ['04', '06', '09', '11']

                # Validation for the date format and values
                if len(expense_date.split('-')) != 3:
                    print("     ☹️  Sorry, you have entered an invalid date!")
                elif expense_date.split('-')[1] not in all_months_budget:
                    print("     ☹️ Sorry, you have not set the budget for this month!")
                elif expense_amt <= 0:
                    print("     ☹️  Sorry, you have provided an invalid amount!")
                elif len(expense_date.split('-')[-1]) != 4:
                    print("     ☹️ Sorry, you have entered an invalid year!")
                elif (expense_date.split('-')[1] in all_months_budget) and \
                     ((expense_date.split('-')[1] in all_month_31_days and 1 <= int(expense_date.split('-')[0]) <= 31) or 
                      (expense_date.split('-')[1] in all_month_30_days and 1 <= int(expense_date.split('-')[0]) <= 30) or 
                      (expense_date.split('-')[1] == '02' and 1 <= int(expense_date.split('-')[0]) <= 29)):  # Handles February
                    diction_expenser = {}
                    diction_expenser["Date"] = expense_date
                    diction_expenser["Amount"] = expense_amt
                    diction_expenser["Place"] = expense_place
                    diction_expenser["Description"] = expense_desc

                    for dico in all_budget_list:
                        if dico["Month Number"] == expense_date.split('-')[1]:
                            remaining_budget = dico["Remaining_Budget"]
                            if expense_amt > remaining_budget:
                                print("      🥶  Your purchase now exceeds the remaining budget for the month!")
                            else:
                                print("      😊  Expense is within the remaining budget!")
                            dico["Remaining_Budget"] -= expense_amt
                            print("       😊 Budget has been updated!")
                            break
                        else:
                            pass

                    diction_expenser["Expense Id"] = "EXPENSO" + str(total_expenses + 1)
                    all_expenses_list.append(diction_expenser)
                    print("      ✅ Expense has been added!")
                    break
                else:
                    print("      ☹️  Sorry, the date you provided is invalid for the selected month!")

            # Saving updated data to files
            filehandler3 = open("budget.dat", "wb")
            filehandler4 = open("expenses.dat", "wb")
            pickle.dump(all_budget_list, filehandler3)
            pickle.dump(all_expenses_list, filehandler4)
            filehandler3.close()
            filehandler4.close()
            filehandler2.close()
        filehandler1.close()
    except FileNotFoundError:
        print("      ☹️  Sorry, the required files are missing!")
    except Exception as e:
        print(f"      An error occurred: {e}")
