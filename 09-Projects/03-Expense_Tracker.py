# ================================
#         EXPENSES TRACKER
# ================================

# How It Works:
# - Expenses are stored as (amount, category) pairs.
# - Data is saved into a text file (expenses.txt).
# - The program loads the file at startup and updates it when new expenses are added.

import os

FILENAME = "expenses.txt"

def load_expenses():
    """Load expenses from file into a list of tuples (amount, category)."""
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                expenses.append((float(amount), category))
    return expenses

def save_expenses(expenses):
    """Save expenses to file."""
    with open(FILENAME, "w") as file:
        for amount, category in expenses:
            file.write(f"{amount},{category}\n")

def add_expense(expenses):
    """Add a new expense with amount and category."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append((amount, category))
        save_expenses(expenses)
        print("Expense added!")
    except ValueError:
        print("Invalid amount, try again.")

def view_expenses(expenses):
    """Display all expenses with total spent."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = sum(amount for amount, _ in expenses)
    print("\nYour Expenses:")
    for i, (amount, category) in enumerate(expenses, start=1):
        print(f"{i}. {amount} - {category}")
    print(f"\n Total Spent: {total}\n")

def main():
    expenses = load_expenses()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
