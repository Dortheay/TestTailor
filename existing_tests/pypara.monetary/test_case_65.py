import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_66(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        list_0 = [str_0, str_0, currency_type_0]
        some_money_0 = module_0.SomeMoney(*list_0)
        money_1 = money_0.abs()
        var_0 = money_1.__round__()
        decimal_0 = module_2.Decimal()
        money_2 = some_money_0.subtract(money_1)

if __name__ == "__main__":
    unittest.main()
