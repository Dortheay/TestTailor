import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_41(self):
        try:
            int_0 = 3183
            str_0 = ''
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.scalar_add(str_0)
            var_0 = None
            money_1 = money_0.scalar_add(var_0)
            decimal_0 = module_1.Decimal()
            str_1 = '3C$bqy}h'
            str_2 = 'C"t~$FwCOIcAyF+[=<}'
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            list_0 = [str_0, str_0, currency_type_0]
            currency_0 = module_2.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_0)
            decimal_1 = currency_0.quantize(decimal_0)
            money_2 = money_0.with_qty(decimal_1)
            some_money_0 = module_0.SomeMoney(*list_0)
            bool_0 = some_money_0.gte(money_2)
            money_3 = money_0.abs()
            money_4 = some_money_0.add(money_2)
            var_1 = money_3.__round__()
            bool_1 = some_money_0.as_boolean()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
