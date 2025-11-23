import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            none_money_0 = module_0.NoneMoney()
            list_0 = []
            none_price_0 = module_0.NonePrice()
            price_0 = none_price_0.multiply(list_0)
            decimal_0 = module_1.Decimal()
            int_0 = price_0.__int__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
