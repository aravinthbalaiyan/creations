Food Ordering System README
This Python script implements a basic food ordering system between a hotel and a customer. The system allows customers to view the menu, place an order, and generate a total bill. Below, you'll find an overview of the script's functionality and how to use it.

How to Use
Initialization:

The hotel class is initialized with a dictionary food_list containing food items and their respective prices.
The customer class is used to collect customer orders.
Menu Display:

To display the menu, choose option 1.
The menu will show the available food items and their prices.
Placing an Order:

To place an order, choose option 2.
The menu will be displayed again, and you can enter the food items you wish to order along with their quantities.
Type 'done' when you have finished ordering.
Total Bill:

To generate the total bill, choose option 3.
The script will calculate the total cost of the items in your order and display it.
Exiting the Program:

To exit the program, choose option 0.


Example
Here's an example of how you can use the script:
1. Show the menu list
2. Enter an order
3. Total bill
0. Exit

Enter your option: 1
------------------------------------------
FOOD       PRICE
------------------------------------------
dosa       30
idly       10
vadai      10
poori      30
------------------------------------------

1. Show the menu list
2. Enter an order
3. Total bill
0. Exit

Enter your option: 2
------------------------------------------
FOOD       PRICE
------------------------------------------
dosa       30
idly       10
vadai      10
poori      30
------------------------------------------
Enter a food name or type 'done' to finish
Enter a food name: dosa
Enter a food quantity: 2
Enter a food name: vadai
Enter a food quantity: 3
Enter a food name: done

1. Show the menu list
2. Enter an order
3. Total bill
0. Exit

Enter your option: 3
-------------------------------------------------
FOOD            QUANTITY            PRICE
-------------------------------------------------
dosa            2                   60
vadai           3                   30
-------------------------------------------------
                           Total bill : 90
-------------------------------------------------

1. Show the menu list
2. Enter an order
3. Total bill
0. Exit

Enter your option: 0

About the Code
The hotel class stores the menu and calculates the total bill.
The customer class collects customer orders.
The script uses a while loop to repeatedly display the menu and process orders until the user chooses to exit.
Feel free to customize the food_list and adapt the code to your specific requirements.

You can use this template as a starting point for your README file. Customize it further if needed, add installation instructions if required, and include any additional information about your code.
