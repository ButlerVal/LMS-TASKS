results = []

def add():
    x = float(input("Enter a number ").strip())
    y = float(input("Enter a number ").strip())
    ans = x + y
    results.append(f"{x} + {y} = {ans}")
    print(ans)

def substract():
    x = float(input("Enter a number ").strip())
    y = float(input("Enter a number ").strip())
    ans = x - y
    results.append(f"{x} - {y} = {ans}")
    print(ans)

def multiply():
    x = float(input("Enter a number ").strip())
    y = float(input("Enter a number ").strip())
    ans = x * y
    results.append(f"{x} * {y} = {ans}")
    print(ans)

def divide():
    x = float(input("Enter a number ").strip())
    y = float(input("Enter a number ").strip())
    try:
        ans = x / y
        results.append(f"{x} / {y} = {ans}")
        print(ans)
    except ZeroDivisionError:
        print("Can't be divided by zero")    

def view_history():
    if not results:
        print("nothing in history")
    else:    
        for i, items in enumerate(results, start=1):
            print(f"{i}. {items} ")    

def main():
    while True:
        print("=====Calculator Menu=====")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = (input("Pick a number from 1-6 ").strip())
        print()

        if choice == "1":
            add()

        elif choice == "2":
            substract()

        elif choice == "3":
            multiply()

        elif choice == "4":
            divide()

        elif choice == "5":
            view_history()        

        elif choice == "6":
            print("Are you sure you want to exit Y/N")
            ans = input("Enter Y to stay or N to exit ").upper().strip()
            if ans == "N":
                main()
            elif ans == "Y":
                print("Goodbye! Thanks for using the Calculator.")
                break
            else:
                print("Invalid input. Please enter Y or N ")               
        
        else:
            print("Invalid option. Please try again.")

    


main()            
