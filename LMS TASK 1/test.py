# List to store expenses
expenses = []

# Function to add a new expense
def add_expense():
    item = input("Enter expense description: ").strip()
    try:
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("Amount cannot be negative.\n")
            return
        expenses.append({"item": item, "amount": amount})
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- All Expenses ---")
    for idx, entry in enumerate(expenses, start=1):
        print(f"{idx}. {entry['item']} - ₦{entry['amount']:.2f}")
    print()

# Function to calculate total and average expenses
def show_total_and_average():
    if not expenses:
        print("No expenses to calculate.\n")
        return
    total = sum(entry["amount"] for entry in expenses)
    average = total / len(expenses)
    print(f"\nTotal Expenses: ₦{total:.2f}")
    print(f"Average Expense: ₦{average:.2f}\n")

# Main menu loop
def main():
    while True:
        print("=== Simple Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total and Average")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        print()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total_and_average()
        elif choice == "4":
            print("Goodbye! Thanks for using the expense tracker.")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.\n")

# Run the program
main()
