
import json
import os
from datetime import datetime

# Personal Expense Tracker
# First Python Project


FILE_NAME = "expenses.json"

CATEGORIES = [
    "Food",
    "Transport",
    "Education",
    "Shopping",
    "Entertainment",
    "Other"
]


# Load saved expenses
def load_expenses():

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            print("Could not read saved data. Starting with an empty list.")
            return []

    return []


# Save expenses
def save_expenses(expenses):

    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):

    print("\n--- ADD NEW EXPENSE ---")

    title = input("Enter expense name: ").strip()

    if not title:
        print("Expense name cannot be empty.")
        return

    print("\nExpense Categories:")

    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    try:
        category_choice = int(input("Select category number: "))

        if category_choice < 1 or category_choice > len(CATEGORIES):
            print("Invalid category selection.")
            return

        category = CATEGORIES[category_choice - 1]

        amount = float(input("Enter amount (LKR): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense_date = input(
            "Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if expense_date == "":
            expense_date = datetime.today().strftime("%Y-%m-%d")
        else:
            datetime.strptime(expense_date, "%Y-%m-%d")

        expense = {
            "title": title,
            "category": category,
            "amount": amount,
            "date": expense_date
        }

        expenses.append(expense)

        save_expenses(expenses)

        print("\nExpense added successfully!")

    except ValueError:
        print("Invalid input. Please enter the correct information.")


# View all expenses
def view_expenses(expenses):

    print("\n--- ALL EXPENSES ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 65)

    for i, expense in enumerate(expenses, start=1):

        print(f"\nExpense {i}")
        print(f"Name     : {expense['title']}")
        print(f"Category : {expense['category']}")
        print(f"Amount   : LKR {expense['amount']:,.2f}")
        print(f"Date     : {expense['date']}")

    print("\n" + "-" * 65)


# Calculate total expenses
def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n--- TOTAL EXPENSES ---")
    print(f"Total spending: LKR {total:,.2f}")


# Show category-wise expenses
def category_summary(expenses):

    print("\n--- CATEGORY SUMMARY ---")

    if not expenses:
        print("No expenses available.")
        return

    category_totals = {}

    for category in CATEGORIES:
        category_totals[category] = 0

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] += amount

    for category, total in category_totals.items():

        if total > 0:
            print(f"{category}: LKR {total:,.2f}")


# Main menu
def main():

    expenses = load_expenses()

    while True:

        print("\n================================")
        print("      PERSONAL EXPENSE TRACKER")
        print("================================")

        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            calculate_total(expenses)

        elif choice == "4":

            category_summary(expenses)

        elif choice == "5":

            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:

            print("Invalid choice. Please try again.")


# Start the application
if __name__ == "__main__":
    main()
