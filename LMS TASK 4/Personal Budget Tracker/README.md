# Personal Budget Tracker

## Overview
The Personal Budget Tracker is a Python-based command-line application designed to help users track and categorize their expenses, calculate totals by category, and generate a monthly budget summary. It incorporates persistent storage using JSON and provides a simple interface to manage financial transactions.

## Features
- **Transaction Management**: Add and view transactions with details such as date, category, and amount.
- **Category-wise Totals**: Automatically group expenses by category and calculate totals.
- **Monthly Budget Summary**: Calculate total expenses, remaining income before and after savings, and target savings based on a user-defined percentage.
- **Data Persistence**: Transactions are saved to and loaded from a `transactions.json` file.
- **Date Handling**: Uses the `datetime` module to handle transaction dates in `YYYY-MM-DD` format.

## Requirements
- Python 3.x
- Standard library modules: `datetime`, `json`, `os`

## Files
- `main.py`: Contains the core application logic, including the `Transaction` class and main menu interface.
- `budget_utils.py`: Utility functions for saving/loading transactions and calculating category totals.
- `transactions.json`: Automatically generated to store transaction data persistently.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Clone or download the project files (`main.py` and `budget_utils.py`) to a directory.
3. No additional dependencies are required.

## Usage
1. Navigate to the project directory in your terminal.
2. Run the application using:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu to:
   - **Add Transaction**: Enter the date (YYYY-MM-DD), category (e.g., Rent, Utilities, Groceries), and amount.
   - **View Transactions**: Display all transactions with their details.
   - **View Monthly Budget Summary**: Input monthly income and savings percentage to see a breakdown of expenses, savings, and remaining income.
   - **Exit**: Save transactions and exit the application.

## Example
```plaintext
=== Personal Budget Tracker ===
1. Add Transaction
2. View Transactions
3. View Monthly Budget Summary
4. Exit
Select an option: 1
Enter transaction date (YYYY-MM-DD): 2025-07-18
Enter category (e.g., Rent, Utilities, Groceries): Rent
Enter amount: 1200
Transaction added: Rent - $1200.00 on 2025-07-18

Select an option: 3
What is your total monthly income? 5000
What percentage of your remaining income do you want to save (e.g., 15 for 15%)? 20

--- Monthly Budget Summary ---
Monthly Income: $5000.00

Category-wise Expenses:
Rent: $1200.00
Utilities: $300.00
Groceries: $400.00

Total Expenses: $1900.00
Remaining Income (before savings): $3100.00
Target Savings Amount: $620.00
Remaining Income (after savings): $2480.00
```

## GitHub Commit Strategy
To push this project to GitHub with multiple commits:
1. **Initial Setup**:
   - Initialize a Git repository: `git init`
   - Create `.gitignore` for Python projects (ignore `*.pyc`, `__pycache__`, `transactions.json`): `echo -e "*.pyc\n__pycache__\ntransactions.json" > .gitignore`
   - Commit: `git add .gitignore && git commit -m "Initial commit with .gitignore"`
2. **Add Core Files**:
   - Add `main.py`: `git add main.py && git commit -m "Add main application with Transaction class and menu"`
   - Add `budget_utils.py`: `git add budget_utils.py && git commit -m "Add utility functions for transaction management"`
3. **Add README**:
   - Add `README.md`: `git add README.md && git commit -m "Add README with project documentation"`
4. **Final Touches**:
   - Make any minor fixes or updates: `git add . && git commit -m "Final tweaks and documentation updates"`
   - Push to GitHub: `git remote add origin <repository-url> && git push -u origin main`

## Notes
- The application assumes valid input for amounts and dates. Invalid inputs (e.g., non-numeric amounts or incorrect date formats) will raise errors and require re-entry.
- Transactions are stored in `transactions.json` after every add operation.
- The budget summary integrates the provided code, adapting it to use dynamically calculated category totals from transactions.

## Future Improvements
- Add input validation for dates and amounts (e.g., ensure amounts are positive, dates are valid).
- Implement a feature to delete transactions.
- Add filtering by date range or category for viewing transactions.
- Enhance the budget summary with visualizations (e.g., using `matplotlib`).
- Add error handling for file operations and JSON parsing.

## License
This project is open-source and available under the MIT License.