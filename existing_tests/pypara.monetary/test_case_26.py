import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            int_0 = 3242
            none_money_0 = module_0.NoneMoney()
            monetary_operation_exception_0 = module_0.MonetaryOperationException()
            none_price_0 = module_0.NonePrice()
            money_0 = none_money_0.positive()
            price_0 = module_0.Price()
            price_1 = price_0.__truediv__(int_0)
            some_price_0 = module_0.SomePrice()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
