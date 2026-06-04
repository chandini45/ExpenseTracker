expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)

        with open("expenses.txt", "a") as file:
            file.write(str(amount) + "\n")

        print("Expense added successfully!")

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        print("Total Spending =", sum(expenses))

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
