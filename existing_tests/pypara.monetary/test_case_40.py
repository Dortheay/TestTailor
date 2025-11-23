import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        try:
            none_money_0 = module_0.NoneMoney()
            decimal_0 = module_1.Decimal()
            decimal_1 = module_1.Decimal()
            money_0 = module_0.Money()
            money_1 = none_money_0.add(money_0)
            money_2 = money_0.round()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
