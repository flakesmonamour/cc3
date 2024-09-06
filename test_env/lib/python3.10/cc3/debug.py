from customer import Customer
from coffee import Coffee
from order import Order


john = Customer("John")
jane = Customer("Jane")
alice = Customer("Alice")


latte = Coffee("Latte")
espresso = Coffee("Espresso")


john.create_order(latte, 5.0)
jane.create_order(latte, 6.5)
john.create_order(espresso, 4.0)
alice.create_order(latte, 7.0)

print(f"Latte num_orders: {latte.num_orders()}")  
print(f"Latte average_price: {latte.average_price()}")  

print(f"John's coffees: {[coffee.name for coffee in john.coffees()]}") 
print(f"Jane's coffees: {[coffee.name for coffee in jane.coffees()]}")  


most_spent_on_latte = Customer.most_aficionado(latte)
if most_spent_on_latte:
    print(f"The customer who spent the most on Latte is {most_spent_on_latte.name}.")
print("No customer has ordered Latte yet.")
