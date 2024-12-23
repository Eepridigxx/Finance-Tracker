#This file is going to have functions related to monthly budget management system!
import pickle

def set_budget():
    try:
        filehandler = open("budget.dat" , "wb")
        filehandler2 = open("expenses.dat" , "wb")
        total_budgets = int(input("\n      Enter the total number of budgets you want to add ➜  "))
        if total_budgets <= 0:
            print("      ❌ Sorry ,  please provide a valid input!")
        else:
            all_budget_list = []
            list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            total_added = 0
            for n in range(total_budgets):
                if total_added == 0:
                    bud_dic = {}
                    month_name = input("\n      Enter the month  name 📆 ➜  ").strip().capitalize()
                    if month_name not in list_of_months:
                        print("      ❌ Oops this month is invalid!")
                    else:
                        #also need to ensure that the budget is not zero or less than that
                        #so we gotta keep taking it infinitly
                        while True:
                            month_budget = float(input(f"      Enter the budget for the month of {month_name} 💵 ➜  "))
                            if month_budget <=0:
                                print("      ⚠️ Sorry , please provide a valid budget!")
                            else:
                                break
                        bud_dic["Name"] = month_name
                        #Adding the month names
                        if bud_dic["Name"] == "January":
                            bud_dic["Month Number"] = '01'
                        elif bud_dic["Name"] == "February":
                            bud_dic["Month Number"] = '02'
                        elif bud_dic["Name"] == "March":
                            bud_dic["Month Number"] = '03'
                        elif bud_dic["Name"] == "April":
                            bud_dic["Month Number"] = '04'
                        elif bud_dic["Name"] == "May":
                            bud_dic["Month Number"] = '05'
                        elif bud_dic["Name"] == "June":
                            bud_dic["Month Number"] = '06'
                        elif bud_dic["Name"] == "July":
                            bud_dic["Month Number"] = '07'
                        elif bud_dic["Name"] == "August":
                            bud_dic["Month Number"] = '08'
                        elif bud_dic["Name"] == "September":
                            bud_dic["Month Number"] = '09'
                        elif bud_dic["Name"] == "October":
                            bud_dic["Month Number"] = '10'
                        elif bud_dic["Name"] == "November":
                            bud_dic["Month Number"] = '11'
                        else:
                            bud_dic["Month Number"] = '12'
                        
                        bud_dic["Budget"] = month_budget
                        bud_dic["Remaining_Budget"] = month_budget
                        all_budget_list.append(bud_dic)
                        total_added = total_added + 1
                        print(f"      ✅ Budget details for the month of {month_name} have been added!\n")
                else:
                    bud_dicy = {}
                    month_name = input("      Enter the  month name 📆 ➜  ").strip().capitalize()
                    if month_name not in list_of_months:
                        print("      ❌ Sorry this month is invalid!")
                    else:
                        for dic in all_budget_list:
                            if dic["Name"] == month_name:
                                print(f"      ⚠️ The budget details for this month have already been added!")
                                break
                        else:
                            month_budget = float(input(f"      Enter the budget details for the month of {month_name} 💵 ➜  "))
                            bud_dicy["Name"] = month_name
                            #adding month number as key too in the dictionary!
                            if bud_dicy["Name"] == "January":
                                bud_dicy["Month Number"] = '01'
                            elif bud_dic["Name"] == "February":
                                bud_dicy["Month Number"] = '02'
                            elif bud_dicy["Name"] == "March":
                                bud_dicy["Month Number"] = '03'
                            elif bud_dicy["Name"] == "April":
                                bud_dicy["Month Number"] = '04'
                            elif bud_dicy["Name"] == "May":
                                bud_dicy["Month Number"] = '05'
                            elif bud_dicy["Name"] == "June":
                                bud_dicy["Month Number"] = '06'
                            elif bud_dicy["Name"] == "July":
                                bud_dicy["Month Number"] = '07'
                            elif bud_dicy["Name"] == "August":
                                bud_dicy["Month Number"] = '08'
                            elif bud_dicy["Name"] == "September":
                                bud_dicy["Month Number"] = '09'
                            elif bud_dicy["Name"] == "October":
                                bud_dicy["Month Number"] = '10'
                            elif bud_dicy["Name"] == "November":
                                bud_dicy["Month Number"] = '11'
                            else:
                                bud_dicy["Month Number"] = '12'

                            bud_dicy["Budget"] = month_budget
                            bud_dicy["Remaining_Budget"] = month_budget
                            all_budget_list.append(bud_dicy)
                            total_added = total_added +1 
                            print(f"      ✅ Details have been added for the month of {month_name}\n")
            #now dumping this list in the binary file
            pickle.dump(all_budget_list , filehandler)
            print("      ✅ Details  have been added!")

        #closing the file handle
        filehandler.close()
        filehandler2.close()
    except ValueError:
        print("      🙊 You seem to have given an invalid value!")


#2 code for appending budget

def append_budget():
    try:

        filehandler = open("budget.dat" , "rb")
        #getting the list containing all the monthly budgets
        all_budget_list = pickle.load(filehandler)
        #list containing all the months
        list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        if all_budget_list == []:
            print("\n      ❌ Sorry , you have not added any monthly budget records yet!")
        else:
            bud_dicy = {}
            while True:
                month_name = input("      Enter the month name 📆 ➜  ").strip().capitalize()
                for dic in all_budget_list:
                    if dic["Name"] == month_name:
                        print("\n      ❌ Sorry , the budget details of this month have been already added!")
                        break
                else:
                    if month_name not in list_of_months:
                        print("\n      ❌ Sorry , this month does not exist!")
                    else:
                        while True:
                            month_budget = float(input(f"      Enter the budget for the month of {month_name} 💵 ➜ "))
                            if month_budget <= 0:
                                print("      ⚠️ Sorry , please provide a valid budget value!")
                            else:
                                break
                        bud_dicy["Name"] = month_name
                        if bud_dicy["Name"] == "January":
                            bud_dicy["Month Number"] = '01'
                        elif bud_dicy["Name"] == "February":
                            bud_dicy["Month Number"] = '02'
                        elif bud_dicy["Name"] == "March":
                            bud_dicy["Month Number"] = '03'
                        elif bud_dicy["Name"] == "April":
                            bud_dicy["Month Number"] = '04'
                        elif bud_dicy["Name"] == "May":
                            bud_dicy["Month Number"] = '05'
                        elif bud_dicy["Name"] == "June":
                            bud_dicy["Month Number"] = '06'
                        elif bud_dicy["Name"] == "July":
                            bud_dicy["Month Number"] = '07'
                        elif bud_dicy["Name"] == "August":
                            bud_dicy["Month Number"] = '08'
                        elif bud_dicy["Name"] == "September":
                            bud_dicy["Month Number"] = '09'
                        elif bud_dicy["Name"] == "October":
                            bud_dicy["Month Number"] = '10'
                        elif bud_dicy["Name"] == "November":
                            bud_dicy["Month Number"] = '11'
                        else:
                            bud_dicy["Month Number"] = '12'

                        #adding month number
                        bud_dicy["Budget"] = month_budget
                        bud_dicy["Remaining_Budget"] = month_budget
                        all_budget_list.append(bud_dicy)
                        print(f"\n      ✅ Details for the month of {month_name} have been added!\n")
                        break
        #dumping the list now through another handle
        filehandler2 = open("budget.dat" , "wb")
        pickle.dump(all_budget_list , filehandler2)
        filehandler2.close()
        filehandler.close()
    
    except ValueError:
        print(f"\n      ❌ You have given an invalid input!")


#3 making a function to  display all the budget details
def display_budget():
    try:
        filehandler = open("budget.dat" , "rb")
        all_budget_list = pickle.load(filehandler)
        if all_budget_list == []:
            print("\n      ⚠️  Sorry there are currently no records of budgets. Press 1 to add new ones!")
        else:
            total_bud_dicos = 0
            for dic in all_budget_list:
                total_bud_dicos = total_bud_dicos + 1
                print()
                print("       📆  Month ➜  " , dic["Name"])
                print("       💰  Budget ➜  " , '₹ ', dic["Budget"])
                print("       🗓️  Month Number ➜  " , dic["Month Number"])
                print("       💰 Remaining Budget ➜  " , '₹ ', dic["Remaining_Budget"])
                print()
            
            #printing the total number of budget records
            print(f"\n     ✅ There are a total of {total_bud_dicos} months' records added by you!")
            #closing the file handle
        filehandler.close()
    except FileNotFoundError:
        print(" \n     ⚠️ Sorry there are currently no budget records added by you . Press 1 to add new ones!")
    except:
        print(" \n      Sorry , you have not added any budgets!")

#4. making a function to update a budget history
def update_budget():
    try:
        filehandler = open("budget.dat" , "rb")
        all_budget_list = pickle.load(filehandler)
        if all_budget_list == []:
            print("\n      ⚠️ Sorry there are no budget records that you can update. Press 1 to start adding new ones!")
        else:
            new_budget_list = []
            list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            month_name = input("\n      Enter the month whose budget you wanna update 📆 ➜   ").strip().capitalize()
            if month_name not in list_of_months:
                print("\n     ⚠️  Sorry ,  this month is invalid!")
            else:
                updated = False
                for dicy in all_budget_list:
                    if dicy["Name"] == month_name:
                        while True:
                            new_month_budget = float(input(f"\n      Enter the new budget for the month of {month_name} 💵 ➜ "))
                            if new_month_budget <= 0:
                                print("\n      ⚠️ Sorry, please provide a valid budget value!")
                            else: 
                                break
                        dicy["Budget"] = new_month_budget
                        dicy["Remaining_Budget"] = new_month_budget
                        new_budget_list.append(dicy)
                        updated = True
                        print(f"\n      ✅ Budget details for the month of {month_name} has been updated successfully!")
                    else:
                        new_budget_list.append(dicy)
                
                if updated == False:
                    print(f"\n      ⚠️ You have not added the budget details for {month_name}!")    
                #now it adding the new budget list 
                filehandler2 = open("budget.dat" , "wb")
                pickle.dump(new_budget_list , filehandler2)
                filehandler2.close()
                filehandler.close()
                
    except FileNotFoundError:
        print("\n      ⚠️ Sorry there are no budget records that you can update. Press 1 to add new ones!")
    except ValueError:
        print(" \n     ⚠️ Sorry , please provide a valid budget value!")
    except:
        print(" \n     ⚠️ Sorry there are  no budget records that you can update. Press 1 to add new ones!")


#function to delete a months's budget history!
def delete_budget_month():
    try:
        #opening in file handle
        filehandler = open("budget.dat" , "rb")
        all_budget_history = pickle.load(filehandler)
        if all_budget_history == []:
            print(" \n    ⚠️  You currently don't have any monthly budget set that can be deleted . Press 1 to set some!")
        else:
            removed = False
            month_name = input("      Enter the month name 🗓️  ").strip().capitalize()
            for dic in all_budget_history:
                if dic["Name"] == month_name:
                    all_budget_history.remove(dic)
                    removed = True
            
            #now opening a new file handler to write content into the budget file!
            filehandler2  = open("budget.dat" , "wb")
            pickle.dump(all_budget_history , filehandler2)
            if removed:
                print(f"\n     ✅  Budget history for the month of {month_name} has been removed!")
            else:
                print(f"\n      ⚠️  Sorry you have not set any monthly budgrt for this month of {month_name}!")
                
    except:
        print("\n       ⚠️  Sorry you have currently not set any monthly budgets!")

#Last function to deal with monthly budgets
def clear_budget_history():
    try:
        filehandler = open("budget.dat" , "rb")
        all_budget_list = pickle.load(filehandler)
        if all_budget_list == []:
            print("\n    👍  Your budget history is already cleared . Press 1 to add new ones!")
        else:
            all_budget_list.clear()
            filehandler2 = open("budget.dat" , "wb")
            print(" \n     👍 Your budget history has been cleared successfully!")
            pickle.dump(all_budget_list , filehandler2)
        
        filehandler.close()
    except:
        print("\n     👍 Your budget history is already cleared. Press 1 to add new ones! ")