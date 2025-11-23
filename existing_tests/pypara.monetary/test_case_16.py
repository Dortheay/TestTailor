import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            int_0 = 3242
            str_0 = ''
            none_money_0 = module_0.NoneMoney()
            list_0 = [none_money_0, none_money_0, str_0]
            some_price_0 = module_0.SomePrice(*list_0)
            bool_0 = some_price_0.as_boolean()
            money_0 = none_money_0.scalar_add(str_0)
            decimal_0 = module_1.Decimal()
            str_1 = '3C$bqy}h'
            str_2 = 'C"t~$FwC$IcAyF+[=<}'
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            int_1 = 1317
            currency_0 = module_2.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
            decimal_1 = currency_0.quantize(decimal_0)
            money_1 = money_0.with_qty(decimal_1)
            bool_1 = money_1.__ge__(money_0)
            money_2 = money_0.abs()
            var_0 = money_2.__round__()
            list_1 = [var_0, var_0]
            none_price_0 = module_0.NonePrice(*list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
