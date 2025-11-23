import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            price_0 = None
            var_0 = None
            none_price_0 = module_0.NonePrice()
            bool_0 = none_price_0.as_boolean()
            price_1 = none_price_0.add(price_0)
            price_2 = none_price_0.scalar_subtract(var_0)
            some_price_0 = module_0.SomePrice()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
