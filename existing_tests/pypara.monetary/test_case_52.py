import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        money_1 = none_money_0.abs()
        var_0 = money_1.__round__()
        bool_0 = money_1.as_boolean()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.round()

if __name__ == "__main__":
    unittest.main()
