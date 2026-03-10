import sys
import unittest
from pathlib import Path
from unittest import mock

ORDER_MGMT_DIR = Path(__file__).resolve().parents[1]
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))
from service.order_service import OrderService
# 设置路径以确保可以导入 service 模块
class TestOrderServiceBasic(unittest.TestCase):
    def test_create_order_interaction(self):
        service = OrderService()
        customer_name = "Alice"
        amount = 100.0
        fixed_id = 999

        # Mock generate_id 以确保测试的可预测性
        with mock.patch("service.order_service.generate_id", return_value=fixed_id):
            service.create_order(customer_name, amount)

        # 验证订单是否已保存且属性正确
        orders = service.get_all_orders()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].order_id, fixed_id)
        self.assertEqual(orders[0].customer_name, customer_name)
        self.assertEqual(orders[0].amount, amount)

if __name__ == "__main__":
    unittest.main()