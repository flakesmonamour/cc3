class Customer:
    _all = [] # A Variable of Class - keeps track of every customer
    def __init__(self, name):
        if isinstance(name, str) and 1<= len(name)<= 15:
            self._name = name
            self._orders =[]
            Customer._all.append(self)
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def create_order(self, coffee, price):
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee) or not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Invalid coffee or price.")
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        customer_spending = {}
        for customer in cls._all:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
        if total_spent > 0:
                customer_spending[customer] = total_spent
        if customer_spending:
            return max(customer_spending, key=customer_spending.get)
        return None

