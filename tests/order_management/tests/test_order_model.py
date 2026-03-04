import sys
import unittest
from pathlib import Path


# Ensure imports like "from model.order import Order" work
ORDER_MGMT_DIR = Path(__file__).resolve().parents[1]
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))


class TestOrderModel(unittest.TestCase):
    def test_order_str_format(self):
        from model.order import Order

        order = Order(order_id=7, customer_name="Alice", amount=100.0)
        self.assertEqual(
            str(order),
            "Order(id=7, customer='Alice', amount=100.0)",
        )


if __name__ == "__main__":
    unittest.main()

