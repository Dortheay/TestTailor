import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_100(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        date_time_0 = module_0.DateTime()

if __name__ == "__main__":
    unittest.main()
