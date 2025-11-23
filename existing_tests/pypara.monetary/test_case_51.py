import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        float_0 = -694.5467
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.positive()
        none_price_1 = module_0.NonePrice()
        price_1 = none_price_1.floor_divide(float_0)

if __name__ == "__main__":
    unittest.main()
