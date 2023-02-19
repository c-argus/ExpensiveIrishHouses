from datetime import datetime
import jason

"""
Dictionary to store data from transactions
"""

transactions = {}


"""
Menu functions
"""

def listTransactions():
    pass

def addTransaction():
    pass

def deleteTransaction():
    pass

def editTransaction():
    pass

def checkBalance():
    pass


"""
Get user to input an option on the menu.
Using ()upper to  converts characters to uppercase,
so the user can input uppercase or not
and it won't get an error message back
"""

"""
Menu created by conditional statements 
to prompt the user to enter their
selection
"""

"""
The options listTransaction, addTransaction and
deleteTransaction will be stored in a dictionary.
"""

while True:
    op = input ("Choose your option on the menu below: \nL - List transactions \nA - Add transaction \nD - Delete transaction \nE - Edit transaction \nC - Check balance \nX - Exit \n\nType here: ").upper()

    if op == 'L':
        listTransactions()
    elif op == 'A':
        addTransactions()
    elif op == 'D':
        deleteTransaction()
    elif op == 'E':
        editTransaction()
    elif op == 'C':
        checkBalance()
    elif op == 'X':
        exit()
    else:
        print("\nUnsupported choice! \n")



