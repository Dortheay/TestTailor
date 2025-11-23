import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_54(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        decimal_0 = module_2.Decimal()
        money_1 = money_0.abs()
        var_0 = money_1.__round__()
        var_1 = None
        money_2 = money_0.__truediv__(var_1)

if __name__ == "__main__":
    unittest.main()
