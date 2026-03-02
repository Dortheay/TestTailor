from service.order_service import OrderService


class OrderController:

    def __init__(self):
        self.order_service = OrderService()

    def create_order(self, customer_name: str, amount: float):
        self.order_service.create_order(customer_name, amount)

    def print_all_orders(self):
        orders = self.order_service.get_all_orders()
        for order in orders:
            print(order)