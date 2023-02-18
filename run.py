"""
Get user to input an option on the menu.
Using ()upper to  converts characters to uppercase, 
so the user can input uppercase or not 
and it won't get an error message back
"""
print ("Choose your option on the menu below:\n")
while True:
    op = input ("L - List transactions \nA - Add transaction \nD - Delete transaction \nE - Edit transaction \nC - Check balance \nE - Exit \n\nType here").upper()