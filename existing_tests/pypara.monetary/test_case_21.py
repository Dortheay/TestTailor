import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            int_0 = 3242
            str_0 = '\n    Type of functions which read chart-of-accounts from a source.\n    '
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.scalar_add(str_0)
            decimal_0 = module_1.Decimal()
            money_1 = money_0.__add__(money_0)
            str_1 = '3C$bqy}h'
            str_2 = 'C"t~$FwC<IcAyF+[=<}'
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            int_1 = 1317
            currency_0 = module_2.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
            decimal_1 = currency_0.quantize(decimal_0)
            money_2 = money_0.with_qty(decimal_1)
            date_0 = None
            money_3 = none_money_0.with_dov(date_0)
            money_4 = money_0.abs()
            var_0 = money_4.__round__()
            some_money_0 = module_0.SomeMoney()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
