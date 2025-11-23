import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'v8UX.'
            none_price_0 = module_0.NonePrice()
            price_0 = none_price_0.scalar_add(str_0)
            none_price_1 = module_0.NonePrice()
            price_1 = none_price_1.multiply(price_0)
            var_0 = price_1.__round__()
            none_money_0 = None
            list_0 = [var_0, price_1, none_money_0, none_money_0]
            none_price_2 = module_0.NonePrice(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
