import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            price_0 = None
            var_0 = None
            none_price_0 = module_0.NonePrice()
            bool_0 = none_price_0.as_boolean()
            price_1 = price_0.__floordiv__(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
