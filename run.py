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
    """
    Get the values from the transactions dictionary
    Print the transactions on the screen
    for the user
    """
    if len(transactions) == 0:
        print("\nNo transactions!")
        return
    print("\nYour transactions: ")

    for data_stored in transactions.values():
        print(f'{data_stored["id"]} - {data_stored["date"]} - {data_stored["name"]}: €{data_stored["value"]:.2f}')    
    

def addTransaction():
    """
    Get transactions data input by the user
    All data stored in a dictionary
    """

    """
    Raises ValueError if strings 
    cannot be converted to float.
    """

    global id_transaction

    name = input('\nTransaction name: ')
    while True:
        try: 
            value = float(input('Transaction value (use a - signal if expenses): '))
            break
        except ValueError:
            print("Invalid data. Please try again.")    
    date = str(datetime.now())

    data_stored = {
        "name": name,
        "value": value,
        "date": date,
        "id": str(id_transaction),
    }

    transactions["id_" + str(id_transaction)] = data_stored
    id_transaction =+ 1
    print("Data stored successfully!\n")


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
    op = input ("""\nChoose your option on the menu below: 
    L - List transactions 
    A - Add transaction 
    D - Delete transaction 
    E - Edit transaction 
    C - Check balance 
    X - Exit 
    \rType here: """).upper()

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



