import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = -9
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.divide(int_0)
            var_0 = money_0.__round__()
            str_0 = 'Indian Rupee'
            list_0 = [var_0, str_0, int_0]
            some_price_0 = module_0.SomePrice(*list_0)
            float_0 = some_price_0.as_float()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
