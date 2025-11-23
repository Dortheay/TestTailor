import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_50(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.positive()
        none_price_0 = module_0.NonePrice()
        bool_0 = none_price_0.as_boolean()
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        list_0 = [str_0, str_0, currency_type_0]
        bool_1 = money_0.__bool__()
        money_1 = money_0.abs()
        some_money_0 = module_0.SomeMoney(*list_0)
        money_2 = money_0.abs()
        money_3 = some_money_0.add(money_1)
        price_0 = none_price_0.round()

if __name__ == "__main__":
    unittest.main()
