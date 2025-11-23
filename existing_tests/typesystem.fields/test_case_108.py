import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_109(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        date_time_0 = module_0.DateTime()
        array_0 = module_0.Array(date_time_0)

if __name__ == "__main__":
    unittest.main()
