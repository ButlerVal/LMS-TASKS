store_items = {
    "Rice": 400,
    "Beans": 300,
    "Oil": 800,
    "Bread": 200,
    "Juice": 1200,
    "Yam": 2000
}

cart_items_list = []

def view_store_items():
    for key, value in store_items.items():
        print(f"{key}: {value}")

def add_items():
    item_name = input("What would you like to purcahse? ").capitalize().strip()
    if item_name in store_items:
        try:
            quantity = int(input(f"Enter the number of {item_name} you'd like "))
            if quantity < 1:
                print("Invalid amount")
                return
            else:
                cart_items_dict = {"items": item_name, "quantity": quantity, "price": store_items[item_name]}
                cart_items_list.append(cart_items_dict)
        except ValueError:
            print("Input value is wrong. Enter a number")
    else:
        print(f"{item_name} not in store")        
    print(f"{item_name} has been added to cart")
    
def view_cart():
    if not cart_items_list:
        print("No items in cart!!")
        return
    print("=====Cart Items=====")
    for cart_item_dict in cart_items_list:
        item_name = cart_item_dict.get("items")
        quantity = cart_item_dict.get("quantity")
        price = cart_item_dict.get("price")
        subtotal = quantity * price
        print()
        print(f"Item name: {item_name}")
        print(f"Item quantity: {quantity}")
        print(f"Item price: {price}")
        print(f"Subtotal: ${subtotal}")

def remove_item():
    item_name = input("Enter the name of item you'll like to remove ? ").strip().capitalize()
    for cart_item_dict in cart_items_list:
        if cart_item_dict.get("items") == item_name:
            cart_items_list.remove(cart_item_dict)
            print(f"{item_name} removed successfully")
            return 
        print(f"{item_name} not in cart")   
        
def clear_cart():
    print("Are you sure you want to clear cart Yes or No")
    ans = input("Enter Yes or No ").strip().capitalize()
    if ans == "Yes":
        cart_items_list.clear()
        print("Cart items cleared successfully")
    elif ans == "No":
        return
    else:
        print("Invalid input. Please enter Yes or No")

def total_bill():
    if not cart_items_list:
        print("No items in cart!!")
        return
    view_cart()
    total = sum((value["quantity"]) * (value["price"]) for value in cart_items_list)
    print(f"Your total bill is ${total} ")

def main():
    while True:
        print()
        print("=====Shopping Menu=====")
        print("1. View Store Items")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Remove Item From Cart")
        print("5. Clear Cart")
        print("6. View Total Bill")
        print("7. Exit")

        choice = (input("Pick a number from 1-7 ").strip())
        print()

        if choice == "1":
            view_store_items()

        elif choice == "2":
            add_items()

        elif choice == "3":
            view_cart()

        elif choice == "4":
            remove_item()

        elif choice == "5":
            clear_cart() 

        elif choice == "6":
            total_bill()           

        elif choice == "7":
            print("Are you sure you want to exit Y/N")
            ans = input("Enter Y to stay or N to exit ").upper().strip()
            if ans == "N":
                main()
            elif ans == "Y":
                print("Goodbye! Thanks for visiting our store.")
                break
            else:
                print("Invalid input. Please enter Y or N ")               
        
        else:
            print("Invalid option. Please try again.")

    


main()            




#add_items()
#print(cart_items_list)  
#view_cart()
#remove_item()



