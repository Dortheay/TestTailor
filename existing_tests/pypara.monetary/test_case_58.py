import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_59(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        decimal_0 = module_2.Decimal()
        bool_0 = money_0.__le__(money_0)
        money_1 = none_money_0.negative()
        money_2 = money_1.round()
        var_0 = money_2.__round__()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.round()
        price_1 = none_price_0.negative()

if __name__ == "__main__":
    unittest.main()
