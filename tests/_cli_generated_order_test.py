import os
import sys
import unittest
from pathlib import Path


# Make `from service.order_service import OrderService` work for the
# order_management example (which uses non-package absolute imports).
repo_root = Path(os.getcwd()).resolve()
ORDER_MGMT_DIR = repo_root / "tests" / "order_management"
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))

from service.order_service import OrderService  # noqa: E402


class CLIGeneratedOrderServiceTest(unittest.TestCase):
    def test_create_order(self):
        s = OrderService()
        s.create_order("Alice", 1.0)


if __name__ == "__main__":
    unittest.main()

