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
    * [Features Left to Implement](features-left-to-implement)
* [User Experience](#user-experience)
    * [User stories](#user-stories)
        * [User goals](#user-goals)
    * [Design](#design)
* [Design](#design)
* [Technologies Used](#technologies-used)   
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Features
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

## Features Left to Implement
* Provide the user the possibility of keeping a Google spreadsheet with all the transactions saved in the app so it can be used for external purposes.
* For *List Transactions*, there will be a new functionality of listing the transactions per month.
* For *Add Transaction* there will be the possibility of adding more than one transaction without returning to the menu, to make it more practical for the user.
* Another feature for the menu will be added to make it possible for the user to edit the transactions.

## User Experience (UX)
The design of the game was all thinking about make things simple for the user. With simple features and clear context to help them navigate through the app.

### User stories
#### User goals
* The main goal is to provide to the users a money management solution in their every day lives.
* It is easy to navigate, making it intuitive for the users, even the ones that are not tech experts.
* It provides error messages if inserting the wrong data, e.g.: inserting words where should be numbers, typing the wrong selection letter or trying to access a list with no date in it.

### Design
* The design of the finance app is simple and straightforward. In the future the possibility of creating graphs based on the date that has been input will be added to make it more visual for the user. The instructions providade to the user make it easy to navigate and the errors messages helps it when needed.
* For the code, it was used loop to iterate throughout the menu features.


