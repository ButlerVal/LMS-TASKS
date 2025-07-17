while True:
    name = input("Enter your name or Done to stop").strip()
    if name == 'Done':
        break
    try:
        age = int(input("How old are you?"))
        if age < 5:
            price = 0
        elif age >= 5 and age <=17:
            price = 5
        elif age >=18 and age <=59:
            price = 10
        else:
            price = 7  

        coupon = input("Do you have a coupon Yes/No")
        discount = 0
        if coupon == 'Yes':
            discount = (price*0.2)
        elif coupon == 'No':
            discount = 0
        else:
            print("Invaild Response Please Enter Yes/No") 
        
        Total = (price - discount)

        print(f"Final Price: ${Total}")           

    except ValueError:
        print("Enter a valid name")  

print("Thanks")