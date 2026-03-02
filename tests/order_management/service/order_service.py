from repository.order_repository import OrderRepository
from model.order import Order
from utils.id_generator import generate_id


class OrderService:

    def __init__(self):
        self.order_repository = OrderRepository()

    def create_order(self, customer_name: str, amount: float):
        order_id = generate_id()
        order = Order(order_id, customer_name, amount)
        self.order_repository.save(order)

    def get_all_orders(self):
        return self.order_repository.find_all()