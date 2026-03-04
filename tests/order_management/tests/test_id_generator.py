import itertools
import sys
import unittest
from pathlib import Path
from unittest import mock


# Ensure imports like "from utils.id_generator import generate_id" work
ORDER_MGMT_DIR = Path(__file__).resolve().parents[1]
if str(ORDER_MGMT_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_MGMT_DIR))


class TestIdGenerator(unittest.TestCase):
    def test_generate_id_is_monotonic_and_starts_at_1_when_reset(self):
        import utils.id_generator as id_generator

        with mock.patch.object(id_generator, "_counter", itertools.count(1)):
            self.assertEqual(id_generator.generate_id(), 1)
            self.assertEqual(id_generator.generate_id(), 2)
            self.assertEqual(id_generator.generate_id(), 3)


if __name__ == "__main__":
    unittest.main()

