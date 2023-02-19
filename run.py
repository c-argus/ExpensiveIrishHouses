from datetime import datetime
import json

"""
Dictionary to store data from transactions
"""

transactions = {}
id_transaction = 1

"""
Menu functions
"""

def listTransactions():
    pass

def addTransaction():
    """
    Get transactions data input by the user
    All data stored in a dictionary
    """
    global id_transaction

    name = input('\nTransaction name: ')
    value = float(input('Transaction value (use a - signal if expenses): '))
    date = str(datetime.now())

    data_stored = {
        "name": name,
        "value": value,
        "date": date,
        "id": str(id_transaction),
    }

    transactions["id_" + str(id_transaction)] = data_stored
    id_transaction =+ 1
    print("Data stored successfully!")

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
        addTransaction()
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



