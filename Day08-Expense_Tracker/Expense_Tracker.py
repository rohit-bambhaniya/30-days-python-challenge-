class ExpenseTracker:

    def __init__(self,):

        self.expenses = []
        self.load_expenses()

    def load_expenses(self):

        try:

            with open("expenses.txt", "r") as file:

                for line in file :
                    
                    category, amount = line.strip().split(",")

                    expense = {
                        "category": category,
                        "amount": float(amount)
                    }

                    self.expenses.append(expense)


        except FileNotFoundError:

            pass
        

    def add_expense(self):
       
       while True:
            
            try :

                item = input("Enter your Expense:-").strip()

                if not item:
                    print("Expense name cannot be empty!")
                    continue
                   

                price = float(input("Enter Expenses price:-"))

                if price <= 0:
                    print("Amount must be greater than 0")
                    continue

                expense = {
                "category": item,
                "amount": price
                }


                self.expenses.append(expense)

                with open("expenses.txt", "a") as file:

                    file.write(f"{item},{price}\n")

                    print("Expense added successfully!")
               

            except ValueError:

                print("Invalid price! Please enter a valid number.")
                continue

            while True:

                again = input("Do you want to add another expense? (y/n): ").lower().strip()

                if again in  ['y', 'n']:
                    break
                
                print("Invalid input! Please enter only 'y' or 'n'.")
                   

            if again == 'n':
                print("Returning to main menu...")
                break

    def save_expenses(self):

        with open("expenses.txt", "w") as file:

            for expense in self.expenses:

                file.write(
                    f"{expense['category']},{expense['amount']}\n"
                )
            
    def view_expenses(self):

        if not self.expenses:
            print("No expenses added yet!")
            return

        print("\n--- Your Expenses ---")
        for index, expense in enumerate(self.expenses, start=1):

            print(f"{index}. {expense['category']} - ₹{expense['amount']:.2f}")

    def delete_expense(self):

        if not self.expenses:
            print("No expenses added yet!")
            return
    
        self.view_expenses()
    
        while True:
        
            try:
                expense_number = int(
                    input("\nEnter expense number to delete: ")
                )
    
                delete_index = expense_number - 1
    
                if delete_index < 0 or delete_index >= len(self.expenses):
                    print("Invalid expense number!")
                    continue
                
                selected_expense = self.expenses[delete_index]
    
                while True:
                
                    confirm = input(
                        f"Are you sure you want to delete "
                        f"'{selected_expense['category']}'? (y/n): "
                    ).lower().strip()
    
                    if confirm in ["y", "n"]:
                        break
                    
                    print("Please enter only 'y' or 'n'.")
    
                if confirm == "y":
                
                    deleted = self.expenses.pop(delete_index)


                    self.save_expenses()
    
                    print(
                        f"Expense deleted successfully: "
                        f"{deleted['category']}"
                    )
    
                else:
                
                    print("Deletion cancelled.")
    
                break
            
            except ValueError:
            
                print("Please enter a valid number!")
    

    def show_total(self):

        if not self.expenses:
            print("No expenses added yet!")
            return

        total = 0

        for expense in self.expenses:

            total += expense["amount"]

        print(f"\nTotal Expenses: ₹{total:.2f}")


def main():

    app = ExpenseTracker()

    print("===== Expense Tracker =====")

    while True:

        menu = """
1. Add Expense
2. View Expenses
3. Show Total
4. Delete Expense
5. Exit
    """

        print(menu)
    
        user = input("Enter your choice:-")

        if user == '1':
            app.add_expense()

        elif user == '2':
            app.view_expenses()

        elif user == '3':
            app.show_total()

        elif user == '4':
            app.delete_expense()

        elif user == '5':
            
            print("Exiting... Goodbye! ")
            break

        else:

            print("Invalid Choice! Please choose between 1 to 5.")
            continue


if __name__=='__main__':
    main()
        








