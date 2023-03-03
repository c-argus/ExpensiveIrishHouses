from datetime import datetime
import json

"""
Dictionary to store data from transactions
Handling exceptions in case json file is blank
"""
def get_transactions():
    with open('transactions.json', 'r') as file:
        return json.loads(file.read())

"""
Menu functions
"""
def list_transactions():
    """
    Get the values from the transactions dictionary
    Print the transactions on the screen
    for the user
    """
    transactions = get_transactions()

    if len(transactions) == 0:
        print("\nNo transactions!")
        return
    print("\nYour transactions: ")
    for data_stored in transactions.values():
        print(f'{data_stored["id"]} - {data_stored["date"]} - {data_stored["name"]}: €{data_stored["value"]:.2f}')


def add_transaction():
    """
    Get transactions data input by the user
    All data stored in a dictionary
    """

    """
    Raises ValueError if strings
    cannot be converted to float.
    """
    transactions = get_transactions()
    name = input('\nTransaction name: ')

    while True:
        try:
            value = float(input('Transaction value (use a - signal if expenses): '))  # noqa E501
            break
        except ValueError:
            print("Invalid data. Please try again.")
    date = str(datetime.now())

    id = str(len(transactions)+1)

    data_stored = {
        "name": name,
        "value": value,
        "date": date,
        "id": id,
    }

    transactions["id" + id] = data_stored
    print("Data stored successfully!\n")
    save_transactions(transactions)

def delete_transaction():
    """
    Request the user to input the id of the
    transaction to be deleted
    """
    transactions = get_transactions()
    #print('>>> delete_transaction')
    #print(transactions)
    id = "id" + input('\nType the id you wish to exclude: ')
    data_stored = transactions.pop(id)
    print(f'Transaction {data_stored["id"]} - "{data_stored["name"]}," €{data_stored["value"]:.2f} was deleted!')

    save_transactions(transactions)
    update_transaction()

def update_transaction():
    transactions = get_transactions()

    updated_transactions = {};
    for i, key in enumerate(transactions):
        index = str((i + 1))
        updated_transactions['id'+index] = transactions[key]
        updated_transactions['id'+index]['id'] = i + 1

    save_transactions(updated_transactions)

def save_transactions(update_transactions):
    """
    Function to save all the data provided by the user
    in a JSON file
    For future checkings, and deleting
    """
    # print('>>>> len(update_transactions)', len(update_transactions))
    if len(update_transactions) > 0:
        with open('transactions.json', 'w') as file:
            file.write(json.dumps(update_transactions))

def check_balance():
    """
    Show balance on screen for the user
    """
    transactions = get_transactions()
    balance = 0
    for transaction in transactions.values():
        balance += transaction["value"]

    print(f'Your balance is €{balance:.2f}')

def Program():

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
    The options listTransaction, add_transaction and
    delete_transaction will be stored in a dictionary.
    """

    while True:
        op = input("""\nChoose your option on the menu below:
        L - List transactions
        A - Add transaction
        D - Delete transaction
        C - Check balance
        E - Exit
        \rType here: """).upper()

        if op == 'L':
            list_transactions()
        elif op == 'A':
            add_transaction()
        elif op == 'D':
            delete_transaction()
        elif op == 'C':
            check_balance()
        elif op == 'E':
            exit()
        else:
            print("\nUnsupported choice! \n")


Program()