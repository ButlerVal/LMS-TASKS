from billings import Product, Cart

def main():
    cart = Cart()
    filename = "billing_data.json"

    while True:
        print("\n=== Small Shop Billing System ===")
        print("1. Add product to cart")
        print("2. View cart and total")
        print("3. Apply discount and view final total")
        print("4. Save bill to file")
        print("5. View previous transactions")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            product = Product(name, float(price), int(quantity))
            cart.add_product(product)

        elif choice == "2":
            print("\n--- Cart Contents ---")
            cart.view_product()
            print(f"Total: {cart.total()}")

        elif choice == "3":
            final_total = cart.apply_discount()
            print(f"Final total after discount (if any): {final_total}")

        elif choice == "4":
            cart.save_bill(filename)

        elif choice == "5":
            cart.view_previous_transactions(filename)

        elif choice == "6":
            print("Goodbye! Thanks for using our Billing System")
            break

        else:
            print("Invalid choice. Please select from 1-6.")

if __name__ == "__main__":
    main()
