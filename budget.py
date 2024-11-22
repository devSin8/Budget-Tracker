import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })
        print("Expense added successfully!")

    def edit_expense(self, index, amount=None, category=None, description=None):
        if 0 <= index < len(self.expenses):
            if amount:
                self.expenses[index]["amount"] = amount
            if category:
                self.expenses[index]["category"] = category
            if description:
                self.expenses[index]["description"] = description
            print("Expense updated successfully!")
        else:
            print("Invalid index!")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            print("Expense deleted successfully!")
        else:
            print("Invalid index!")

    def display_expenses(self):
        print("\nExpenses:")
        for i, expense in enumerate(self.expenses):
            print(f"{i}. {expense['date']} - ${expense['amount']} - {expense['category']} - {expense['description']}")
        print()

    def display_total_monthly_expenses(self):
        current_month = datetime.datetime.now().strftime("%Y-%m")
        total = sum(exp["amount"] for exp in self.expenses if exp["date"].startswith(current_month))
        print(f"\nTotal Expenses for {current_month}: ${total}\n")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. Display All Expenses")
        print("5. Display Total Monthly Expenses")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., food, utilities, rent): ")
                description = input("Enter description: ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif choice == "2":
            tracker.display_expenses()
            try:
                index = int(input("Enter the index of the expense to edit: "))
                amount = input("Enter new amount (or press Enter to skip): ")
                category = input("Enter new category (or press Enter to skip): ")
                description = input("Enter new description (or press Enter to skip): ")
                tracker.edit_expense(
                    index,
                    float(amount) if amount else None,
                    category if category else None,
                    description if description else None
                )
            except ValueError:
                print("Invalid input. Please enter a valid index or amount.")

        elif choice == "3":
            tracker.display_expenses()
            try:
                index = int(input("Enter the index of the expense to delete: "))
                tracker.delete_expense(index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "4":
            tracker.display_expenses()

        elif choice == "5":
            tracker.display_total_monthly_expenses()

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
