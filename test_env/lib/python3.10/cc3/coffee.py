class Coffee:
    _all = []  # Keep all the coffees

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            self._orders =[]
            Coffee._all.append(self)
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
      orders = self.orders()
      if orders:
            total_price = sum(order.price for order in orders)
            return total_price / len(orders)
      return 0
