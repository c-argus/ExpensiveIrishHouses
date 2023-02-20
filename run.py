from datetime import datetime
import json

"""
Dictionary to store data from transactions
Handling exceptions in case json file is blank
"""
try:
    with open('transactions.json', 'r') as file:
        transactions = json.loads(file.read())

    id_transaction = transactions["idtransaction"]
    transactions.pop("idtransaction")
except:
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
    """
    Request the user to input the id of the
    transaction to be deleted 
    """
    id = "id_" + input('\nType the id you wish to exclude: ')
    data_stored = transactions.pop(id)
    print(f'Transaction{data_stored[id]} - "{data_stored["name"]}," €{data_stored["value"]:.2f} was deleted!')

def editTransaction():
    pass

def checkBalance():
    """
    Show balance on screen for the user
    """
    balance = 0
    for transaction in transactions.values():
        balance += transaction["value"]

    print(f'Your balance is €{balance:.2f}')

def saveTransactions():
    """
    Function to save all the data provided by the user
    in a JSON file
    For future checkings, and deleting
    """

    c = transactions.copy()
    c["idtransaction"] = id_transaction

    with open('transactions.json', 'w') as file:
        file.write(json.dumps(c))


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
        saveTransactions()
    elif op == 'D':
        deleteTransaction()
        saveTransactions()
    elif op == 'E':
        editTransaction()
        saveTransactions()
    elif op == 'C':
        checkBalance()
    elif op == 'X':
        exit()
    else:
        print("\nUnsupported choice! \n")



