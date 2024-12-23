import pickle

#other functions regarding the expenses and all
#function to display all the expenses!
def display_expense():
    try:
        filehandler = open("expenses.dat" , "rb")
        all_budget_list = pickle.load(filehandler)
        if all_budget_list == []:
            print("       ⚠️  Sorry , there are currently no expenses that have been added by you!")
        else:
            for dic in all_budget_list:
                print("      📆  Date ➜ " , dic["Date"])
                print("      💰  Amount ➜ " , dic["Amount"])
                print("      🏡  Place ➜ " , dic["Place"])
                print("      🗒️  Description ➜ " , dic["Description"])
                print("      ⌨️  Expense Id ➜ " , dic["Expense Id"])
                print()
            
            print(f"      🤓 There are a total of {len(all_budget_list)} expense records added by you!")
                
    except FileNotFoundError:
        print("      😔  Sorry ,  you have not added any expenses yet! Press 7 to add new ones!")
    except ValueError:
        print("        ⚠️ Seems like you have given an invalid value!")


def delete_expense():
    try:
        filehandler = open("expenses.dat" , "rb")
        all_expenses_list = pickle.load(filehandler)
        if all_expenses_list == []:
            print("      ⚠️ There are currently no records that you have added that can be deleted!")
        else:
            filehandler2 = open("budget.dat" , "rb")
            all_budget_list = pickle.load(filehandler2)
            print("\n       Following are the expenses that you have added ⬇️  ")
            for dic in all_expenses_list:
                print("      📆  Date ➜ " , dic["Date"])
                print("      💰  Amount ➜ " , dic["Amount"])
                print("      🏡  Place ➜ " , dic["Place"])
                print("      🗒️  Description ➜ " , dic["Description"])
                print("      ⌨️  Expense Id ➜ " , dic["Expense Id"])
                print()
              
            
            #taking the expense id that the user wants to be deleted
            deleter_id = input("      Enter the Expense Id that you want to delete  ➜ ").strip()
            deleted = False
            for diction in all_expenses_list:
                if diction["Expense Id"] == deleter_id:
                    month_deleted = diction["Date"].split('-')[1]
                    for diker in all_budget_list:
                        if diker["Month Number"] == month_deleted:
                            diker["Remaining_Budget"] += diction["Amount"]
                            print("       💸 The remaining budget has been updated!")
                            break
                    all_expenses_list.remove(diction)
                    print(f"      ✅ The expense with the expense id : {deleter_id} , dated : {diction["Date"]} has been removed!")
                    deleted = True  
            if deleted == False:
                print("        Sorry this expense id is invalid!")
            
            #now adding the expense list back into the file
            filehandler2 = open("expenses.dat" , "wb")
            filehandler3 = open("budget.dat" , "wb")
            pickle.dump(all_expenses_list , filehandler2)
            pickle.dump(all_budget_list , filehandler3)
            #closing all the filehandles
            filehandler2.close()
        filehandler.close()

    except FileNotFoundError:
        print("     😕  Sorry , there are currenty no expense records that can be removed!")
    except ValueError:
        print("     😕 You seem to have provided a wrong input!")


def clear_all_expenses():
    try:
        filehandler = open("expenses.dat" , "rb")
        all_expenses_list = pickle.load(filehandler)
        if all_expenses_list == []:
            print("    😕  You already don't have any expense records!")
        else:
            all_expenses_list.clear()
            filehandler2 = open("expenses.dat" , "wb")
            pickle.dump(all_expenses_list , filehandler2)
            print("     👍 Your expense history has been cleared!\n")
            filehandler2.close()

        #closing all the filehandles
        filehandler.close()

    except FileNotFoundError:
        print("       ✅ All expenses have been already removed from the list!")
    except ValueError:
        print("     😕 Sorry , you seem to have given an invalid expense!")
    except:
        print("😕 Sorry, there are currently no expenses added!")


def search_by_place():
    try:
        filehandler = open("expenses.dat" , "rb")
        all_expense_list = pickle.load(filehandler)
        if all_expense_list == []:
            print("      😕 There are currently no expenses added by you!")
        else:
            place = input("       Enter the place where you want to know you spent 🏡 :  ")
            total_times = 0
            for dic in all_expense_list:
                if dic["Place"] == place.strip().capitalize():
                    print("      📆  Date ➜ " , dic["Date"])
                    print("      💰  Amount ➜ " , dic["Amount"])
                    print("      🏡  Place ➜ " , dic["Place"])
                    print("      🗒️  Description ➜ " , dic["Description"])
                    print("      ⌨️  Expense Id ➜ " , dic["Expense Id"])
                    print()
                    total_times = total_times + 1
                else:
                    pass

            if total_times == 0:
                print("        😕 Sorry you have not ever spent on this place!")
            else:
                amount_spent = 0
                for dic in all_expense_list:
                    if dic["Place"] == place.strip().capitalize():
                        amount_spent = amount_spent + dic["Amount"]
                else:
                    print("       🤓 You have spent  ₹ " , amount_spent , "    place!")

                print(f"      🥂 You have spent {total_times} on this place {place}!")

    except ValueError:
        print("     😕  Seems like you have given an invalid value!")
    except FileNotFoundError:
        print("      😕 There are no expense records currently added by you!")
    except:
        print("     😕 Sorry there are currently no expenses added!")



def purpose_program():
    print('''✉️ 📜 The purpose of our expense tracker program is to be able to give
          individuals specially students using it the capability to store their daily expenses which can help
          them keep track of their monthly budget compelling them to spend money in
          limits. Apart from that the program has been made in using complete
          Python fundamentals such as "PICKLE" module and binary files to save data.
           ✉️ 📜 ''')