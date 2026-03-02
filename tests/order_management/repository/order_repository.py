class OrderRepository:

    def __init__(self):
        self._orders = []

    def save(self, order):
        self._orders.append(order)

    def find_all(self):
        return self._orders