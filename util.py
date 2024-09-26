import pandas as pd

def getCSV():
    try:
        return pd.read_csv("expenses.csv")
    except FileNotFoundError:
        pd.DataFrame(columns=["Index","Date", "Payment Method", "Paid To", "Transaction ID", "Description", "Amount Paid", "Running Total"]).to_csv("expenses.csv", index=False)

        return pd.read_csv("expenses.csv")
    
    
def getRunningTotal(expenseCSV, amount):
    try:
        return expenseCSV['Running Total'].iloc[-1] + amount
    except IndexError:
        return amount

def getNewIndex(expenseCSV):
    try:
        return expenseCSV.iloc[-1]['Index'] + 1
    except IndexError:
        return 1

def updateCSV(expenseCSV : pd.DataFrame, expense : dict):
    expense = pd.DataFrame(expense, index=[0])
    expenseCSV = pd.concat([expenseCSV, expense], ignore_index=True)
    expenseCSV.to_csv("expenses.csv", index=False)
    
def getExpenseAmount():
    while True:
        try:
            amount = float(input("Enter the amount of the expense: "))
            break
        except ValueError:
            print("Please enter a valid amount.")
    return amount
