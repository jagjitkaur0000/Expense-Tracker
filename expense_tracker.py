import os
from datetime import datetime

FILE_NAME = "expenses.txt"
def add_expense():
    amount = input("Enter amount (₹): ")
    category = input("Enter category (e.g. Food, Transport, Shopping): ")
    date = input("Enter date (YYYY-MM-DD): ")

    if not amount or not category or not date:
        print("⚠️ Please fill all fields!\n")
        return

    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{amount},{category},{date}\n")
        print("✅ Expense added successfully!\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")

def view_expenses():
    print("\n📋 All Expenses:")
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    if not lines:
        print("No expenses yet.\n")
    else:
        for line in lines:
            a, c, d = line.strip().split(",")
            print(f"₹{a} - {c} on {d}")
    print()

def view_total_spent():
    print("\n💰 Total Spent:")
    if not os.path.exists(FILE_NAME):
        print("No data to calculate.\n")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            a, _, _ = line.strip().split(",")
            total += float(a)
    print(f"Total Spent: ₹{total}\n")

def view_by_category():
    print("\n📊 Spending by Category:")
    if not os.path.exists(FILE_NAME):
        print("No data to analyze.\n")
        return

    category_totals = {}
    with open(FILE_NAME, "r") as file:
        for line in file:
            a, c, _ = line.strip().split(",")
            category_totals[c] = category_totals.get(c, 0) + float(a)

    if category_totals:
        for cat, amt in category_totals.items():
            print(f"{cat}: ₹{amt}")
    else:
        print("No expenses found.")
    print()

def main():
    while True:
        print("=== 💸 Expense Tracker CLI ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. View by Category")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total_spent()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
