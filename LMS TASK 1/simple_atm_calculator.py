account_balance = 1000

while True:
    print("----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${account_balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            account_balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: $"))
        if amount > account_balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            account_balance -= amount
            print(f"${amount} withdrawn successfully.")

    elif choice == "4":
        print(f"Thank you for using our ATM.")
        print(f"Your final balance is: ${account_balance}")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")
