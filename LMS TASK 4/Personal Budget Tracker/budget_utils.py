import os
import json
from datetime import datetime

def save_transactions(transactions, filename):
    data = [t.to_dict() for t in transactions]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_transactions(filename):
    from main import Transaction
    transactions = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            transactions = [Transaction.from_dict(d) for d in data]
    return transactions

def calculate_category_totals(transactions):
    category_totals = {}
    for t in transactions:
        category = t.category
        amount = t.amount
        category_totals[category] = category_totals.get(category, 0) + amount
    return category_totals