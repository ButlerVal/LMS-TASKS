import json
from datetime import datetime
from budget_utils import save_transactions, load_transactions, calculate_category_totals

class Transaction:
    def __init__(self, date, category, amount):
        self.date = datetime.strptime(date, "%Y-%m-%d") if isinstance(date, str) else date
        self.category = category
        self.amount = float(amount)

    def to_dict(self):
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data):
        return Transaction(data["date"], data["category"], data["amount"])

def add_transaction(transactions):
    date = input("Enter transaction date (YYYY-MM-DD): ").strip()
    category = input("Enter category (e.g., Rent, Utilities, Groceries): ").strip().capitalize()
    amount = float(input("Enter amount: ").strip())
    transaction = Transaction(date, category, amount)
    transactions.append(transaction)
    print(f"Transaction added: {category} - ${amount:.2f} on {date}\n")
    return transactions

def view_transactions(transactions):
    if not transactions:
        print("No transactions found.\n")
        return
    print("\n--- All Transactions ---")
    for idx, t in enumerate(transactions, start=1):
        print(f"{idx}. {t.date.strftime('%Y-%m-%d')} | {t.category} | ${t.amount:.2f}")
    print()

def monthly_budget_summary(transactions):
    monthly_income = float(input("What is your total monthly income? ").strip())
    saving_percentage = float(input("What percentage of your remaining income do you want to save (e.g., 15 for 15%)? ").strip()) / 100

    category_totals = calculate_category_totals(transactions)
    total_expenses = sum(category_totals.values())

    remaining_income_before_savings = monthly_income - total_expenses
    target_savings_amount = remaining_income_before_savings * saving_percentage
    remaining_income_after_savings = remaining_income_before_savings - target_savings_amount

    print("\n--- Monthly Budget Summary ---")
    print(f"Monthly Income: ${monthly_income:.2f}")
    print("\nCategory-wise Expenses:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Remaining Income (before savings): ${remaining_income_before_savings:.2f}")
    print(f"Target Savings Amount: ${target_savings_amount:.2f}")
    print(f"Remaining Income (after savings): ${remaining_income_after_savings:.2f}\n")

def main():
    filename = "transactions.json"
    transactions = load_transactions(filename)

    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Monthly Budget Summary")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            transactions = add_transaction(transactions)
            save_transactions(transactions, filename)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            monthly_budget_summary(transactions)
        elif choice == "4":
            save_transactions(transactions, filename)
            print("Goodbye! Thanks for using the Personal Budget Tracker.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()