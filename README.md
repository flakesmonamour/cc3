#Coffee Shop Order System

#Introduction
This project simulates a coffee shop's order system,
allowing customers to place orders for various coffee drinks.The project implements object relationship between `Customer`,`Coffee` and `Order`.

# Folder Structure
- `Customer.py`:Contains the ` Customer` class.
- `Order.py`:Contains the ` Order` class.
- `debug.py`:A script to test the implemented methods.
-` Coffee.py`:Contains the ` Coffee` class.

#Setup instructions
1.Install dependancies:
pipenv install
2.Activate the environment
pipenv shell
3.Run tests with:

#Method Description
-**Customer**
-`create_order`:Creates an order for a customer.
-`orders`:Returns all orders for the customers.
-`coffees`:Returns unique coffees the customers has ordered.
-`most_aficionado`:Finds the customer who has spent the most on a coffee.

-**Coffee**
-`orders`:Returns all order for a specific coffee.
-`customers`:Returns unique coffees who ordered that coffee.
-`num_orders`:Returns the total number of orders for the coffee.
-`average_price`:Calculates the average price of the coffee's orders.

-**orders**
-`customers`:Returns the customers for the order.
-`coffee`:Returns the coffee for the order
-`price`:Returns the price of the order

##Bonus Method
The `most_aficionado` method allows findings the customer who spent the most money on a given coffee.
