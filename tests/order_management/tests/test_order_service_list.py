import sys
import unittest
from pathlib import Path

ORDER_MGMT_DIR = Path(__file__).resolve().parents[1]
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))
from service.order_service import OrderService

class TestOrderServiceList(unittest.TestCase):
    def test_get_all_orders_returns_multiple(self):
        service = OrderService()
        
        # 初始状态应为空    
        self.assertEqual(len(service.get_all_orders()), 0)

        # 创建多个订单
        service.create_order("User1", 50.0)
        service.create_order("User2", 150.0)
        service.create_order("User3", 300.0)

        # 验证返回的列表长度是否正确
        orders = service.get_all_orders()
        self.assertEqual(len(orders), 3)
        self.assertEqual(orders[0].customer_name, "User1")
        self.assertEqual(orders[1].customer_name, "User2")
        self.assertEqual(orders[2].customer_name, "User3")

if __name__ == "__main__":
    unittest.main()