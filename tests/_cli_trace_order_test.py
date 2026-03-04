import os
import sys
import unittest
from pathlib import Path


# Allow `from service.order_service import OrderService` to work when this
# file is executed from source via exec(...) (no __file__ defined).
repo_root = Path(os.getcwd()).resolve()
ORDER_MGMT_DIR = repo_root / "tests" / "order_management"
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))

from service.order_service import OrderService  # noqa: E402


class TraceOrderServiceTest(unittest.TestCase):
    def test_create_order(self):
        s = OrderService()
        s.create_order("Alice", 3.14)


if __name__ == "__main__":
    unittest.main()

