import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            str_0 = ''
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.scalar_add(str_0)
            decimal_0 = module_1.Decimal()
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            bool_0 = money_0.gt(money_0)
            list_0 = [str_0, str_0, currency_type_0]
            bool_1 = money_0.__bool__()
            some_money_0 = module_0.SomeMoney(*list_0)
            money_1 = some_money_0.abs()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
