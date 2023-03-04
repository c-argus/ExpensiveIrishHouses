# "Expensive Irish Houses" Finances app

## About
This app was inspired by my own experience of trying to save money to achieve the goal of buying a house. It can be used for anyone who wants to save some money.
With a clean visual the user will be able to see, delete in form of a list all the transactions that were saved. As well as checking the most recent balance.

The live website on Heroku can be accessed at the following link: [Live Website on Heroku](https://expensive-irish-houses.herokuapp.com/)

## Content
* [Introduction](#expensive-irish-houses-finances-app)
* [Features](#features)
    * [Menu](#menu)
        * [List Transactions](#list-transactions)
        * [Add Transaction](#add-transaction)
        * [Delete Transaction](#delete-transaction)
        * [Check Balance](#check-balance)
        * [Exit](#exit)
* [User Experience](#user-experience)
* [Design](#design)
* [Technologies Used](#technologies-used)   
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Features
## Menu
* The inicial input request the user to select an option.
* Despite of the menu options beein in capital letter, the user can input also in lowercase without getting an error message.

![Menu](./assets/images/menu_eih.JPG)

* If a non-correspondent letter is pressed, a validation message appears informing the user and they get to choose it again from the options on the menu.

![Menu_error_message](./assets/images/menu_error_eih.JPG)

### **List Transactions**
* This feature print the transactions on the screen for the user.

![List](./assets/images/list_eih.JPG)

* If the transactions list is empty, the user will get a validation message informing about it.

![Menu_validation](./assets/images/menu_validation_eih.JPG)

### **Add Transaction**
* If the user choose to add a transaction it will be requested to insert a description and an amount. In case on an expense the user has to use the minus sign.

![Add](./assets/images/add_eih.JPG)

* In this section, if the user insert characters instead of number for the amount, it will get a validation message and will be requested to insert the amount again.

![Add_error](./assets/images/add_error_eih.JPG)

### **Delete Transaction**
* If the user wish to delete a transaction from the list the delete selection will do that. 
* What the user needs to do is choose the ID for the transaction. 
* After deleting the transaction the user will get a message with the information about what was deleted.
* Once a transaction is deleted, the transactions list will be updated.

![Delete](./assets/images/delete_eih.JPG)

### **Check Balance**
* The check balance input shows on the screen the user's balance.

![Balance](./assets/images/balance_eih.JPG)

### **Exit**
* The exit input, exit the application.

![Exit](./assets/images/exit_eih.JPG)