class Order:

    def __init__(self, order_id: int, customer_name: str, amount: float):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def __str__(self):
        return f"Order(id={self.order_id}, customer='{self.customer_name}', amount={self.amount})"