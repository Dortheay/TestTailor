import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        internet_0 = module_0.Internet()
        var_0 = internet_0.stock_image()

if __name__ == "__main__":
    unittest.main()
