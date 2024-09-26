#!/usr/bin/env python3

# Importing the required modules
from util import getCSV, getRunningTotal, getNewIndex, updateCSV, getExpenseAmount
from messages import successMessage

def main():
    def menu():
        print("1. Add Expense")
        print("2. View Expenses Analysis")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        return choice
    while True:
        choice = menu()
        if choice == 1:
            add_expense()
        elif choice == 2:
            pass
        elif choice == 3:
            break

def add_expense():
    date = input("Enter the date of the expense: ")
    paymentMethod = input("Enter the payment method: ")
    paidTo = input("Enter the name of the person or company to whom the payment was made: ")
    transactionID = input("Enter the transaction ID: ")
    description = input("Enter the description of the expense: ")
    amount = getExpenseAmount()

    expenseCSV = getCSV()
    runningTotal = getRunningTotal(expenseCSV, amount)
    index = getNewIndex(expenseCSV)

    expense = {"Index": index, "Date": date, "Payment Method": paymentMethod, "Paid To": paidTo, "Transaction ID": transactionID, "Description": description, "Amount Paid": amount, "Running Total": runningTotal}
    updateCSV(expenseCSV, expense)
    
    successMessage(200)
    print("Running total: ", runningTotal)

def view_expense_analysis():
    pass
    
if __name__ == "__main__":
    main()