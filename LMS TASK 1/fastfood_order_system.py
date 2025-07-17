user_count = 0

while True:
    user_name = input("Enter your Name or type exit to stop the program").strip()
    if user_name == 'exit':
        break

    else:
        num_burger = int(input("How many burgers would you like"))
        num_fries = int(input("How many fires would you like"))
        num_drinks = int(input("How many drinks would you like"))
        
        total_burger = (num_burger*5)
        total_fries = (num_fries*2)
        total_drinks = (num_drinks*1.5)
        subtotal = total_burger + total_fries  + total_drinks
        discounted_total = 0

        if subtotal > 20:
            discounted_total = subtotal - (subtotal*0.1)
            total = discounted_total
        else:
            total = subtotal
        
        print(f"------- Bill Summary For {user_name} -------")
        print(f"Burger Ordered: {num_burger}")
        print(f"Fries Ordered: {num_fries}")
        print(f"Drinks Ordered: {num_drinks}")
        print(f"Burger Price: ${total_burger}")
        print(f"Fries Price: ${total_fries}")
        print(f"Drinks Price: ${total_drinks}")
        if discounted_total > 0:
            print(f"Discount: ${(subtotal*0.1)}")
        print(f"Total Price: ${total}")
        print("-------------------------------")
        print("Enjoy Your Meal !!")
        user_count+=1

    

print(f"{user_count} people were served")    

    