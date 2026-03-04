import sys
import unittest
from pathlib import Path
from unittest import mock


# Ensure imports like "from service.order_service import OrderService" work
ORDER_MGMT_DIR = Path(__file__).resolve().parents[1]
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))


class TestOrderRepository(unittest.TestCase):
    def test_save_and_find_all(self):
        from repository.order_repository import OrderRepository
        from model.order import Order

        repo = OrderRepository()
        o1 = Order(1, "Alice", 100.0)
        o2 = Order(2, "Bob", 250.0)

        repo.save(o1)
        repo.save(o2)

        self.assertEqual(repo.find_all(), [o1, o2])


class TestOrderService(unittest.TestCase):
    def test_create_order_saves_order_with_generated_id(self):
        from service.order_service import OrderService

        service = OrderService()

        # Patch the already-imported name in service.order_service module.
        with mock.patch("service.order_service.generate_id", return_value=42):
            service.create_order("Alice", 123.45)

        orders = service.get_all_orders()
        self.assertEqual(len(orders), 1)
        order = orders[0]
        self.assertEqual(order.order_id, 42)
        self.assertEqual(order.customer_name, "Alice")
        self.assertEqual(order.amount, 123.45)


class TestOrderController(unittest.TestCase):
    def test_create_order_delegates_to_service(self):
        from controller.order_controller import OrderController

        controller = OrderController()
        controller.order_service = mock.Mock()

        controller.create_order("Alice", 100.0)
        controller.order_service.create_order.assert_called_once_with("Alice", 100.0)

    def test_print_all_orders_prints_each_order(self):
        from controller.order_controller import OrderController
        from model.order import Order

        controller = OrderController()
        controller.order_service = mock.Mock()
        o1 = Order(1, "Alice", 100.0)
        o2 = Order(2, "Bob", 250.0)
        controller.order_service.get_all_orders.return_value = [o1, o2]

        with mock.patch("builtins.print") as p:
            controller.print_all_orders()

        self.assertEqual(p.call_count, 2)
        # `print(order)` passes the object; `__str__` is applied by print().
        p.assert_any_call(o1)
        p.assert_any_call(o2)


if __name__ == "__main__":
    unittest.main()

