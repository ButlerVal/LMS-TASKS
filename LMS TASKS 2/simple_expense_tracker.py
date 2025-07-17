expenses_list = []

def add_expense():
    description = input("Enter description of the expense ").strip().capitalize()
    try:
        amount_value = float(input(f"Enter the amount for {description} "))
        if amount_value < 0:
            print(f"{amount_value} must be greater than Zero")
            return
        expenses_dict = {"item": description, "amount": amount_value}
        expenses_list.append(expenses_dict)
        print("Expense has been added")

    except (ValueError, TypeError):
        print("Input value is wrong. Enter a number")

        
def view_all_expense():
    if len(expenses_list) < 1:
        print("No expense yet")
    else:
        for expenses_dict in expenses_list:
            print("-----All Expenses-----")
            name = expenses_dict.get("item")
            value = expenses_dict.get("amount")
            print(f"{name} is ${value}")

def show_totalAverage():
    if not expenses_list:
        print("No expenses to calculate")
        return
    total = sum(value["amount"] for value in expenses_list)
    average = total/len(expenses_list)
    print(f"Total Expense: ${total}")
    print()
    print(f"Average Expense: ${average}")

def main():
    while True:
        print("=====System Menu=====")
        print("1. Add Expenses")
        print("2. Show All Expenses")
        print("3. Total and Average Expenses")
        print("4. Exit")

        choice = (input("Pick a number from 1-4 ").strip())
        print()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_all_expense()

        elif choice == "3":
            show_totalAverage()

        elif choice == "4":
            print("Are you sure you want to exit Y/N")
            ans = input("Enter Y to stay or N to exit ").upper().strip()
            if ans == "N":
                main()
            elif ans == "Y":
                print("Goodbye! Thanks for using the expense tracker.")
                break
            else:
                print("Invalid input. Please enter Y or N ")               
        
        else:
            print("Invalid option. Please try again.")

    


main()            


#add_expense()
#view_all_expense()
