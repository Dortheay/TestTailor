import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = False
            none_price_0 = module_0.NonePrice()
            bool_1 = none_price_0.is_equal(bool_0)
            str_0 = '`)ElX% FzAS'
            list_0 = [str_0]
            none_money_0 = module_0.NoneMoney(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
