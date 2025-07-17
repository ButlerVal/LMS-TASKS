import math

import json

from datetime import datetime

import os

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.subtotal = self.price * self.quantity

    def __str__(self):
        return f"Item name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Subtotal: {self.subtotal}"

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.quantity} units of {product.name} added successfully.")

    def view_product(self):
        if not self.products:
            print("Cart is empty.")
        else:
            for product in self.products:
                print(product)

    def total(self):
        raw_total = sum(product.subtotal for product in self.products)
        return math.ceil(raw_total)

    def apply_discount(self):
        total_amount = self.total()
        if total_amount > 10000:
            discount = total_amount * 0.05
            discounted_total = total_amount - discount
            print(f"Discount of 5% applied. You saved {discount:.2f}.")
            return math.ceil(discounted_total)
        else:
            print("No discount applied.")
            return total_amount

    def save_bill(self, filename):
        bill_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "products": [
                {
                    "name": product.name,
                    "price": product.price,
                    "quantity": product.quantity,
                    "subtotal": product.subtotal
                }
                for product in self.products
            ],
            "total": self.total(),
            "final_total_after_discount": self.apply_discount()
        }

        if os.path.exists(filename):
            with open(filename, "r") as file:
                bills = json.load(file)
        else:
            bills = []

        bills.append(bill_data)

        with open(filename, "w") as file:
            json.dump(bills, file, indent=4)

        print("Bill saved successfully.")

    def view_previous_transactions(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                bills = json.load(file)
                for i, bill in enumerate(bills, start=1):
                    print(f"\n--- Transaction {i} ---")
                    print(f"Date: {bill['timestamp']}")
                    for product in bill['products']:
                        print(f"{product['quantity']} units of {product['name']} at {product['price']} each. Subtotal: {product['subtotal']}")
                    print(f"Total: {bill['total']}, Final after discount: {bill['final_total_after_discount']}")
        else:
            print("No previous transactions found.")
    