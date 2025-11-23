import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            none_money_0 = module_0.NoneMoney()
            money_0 = None
            money_1 = none_money_0.scalar_subtract(money_0)
            bool_0 = none_money_0.gte(money_1)
            float_0 = none_money_0.as_float()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
