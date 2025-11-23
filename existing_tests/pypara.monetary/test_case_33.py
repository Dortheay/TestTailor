import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            int_0 = 3217
            decimal_0 = module_1.Decimal()
            none_price_0 = module_0.NonePrice()
            bool_0 = none_price_0.as_boolean()
            str_0 = '3C$bqy}h'
            str_1 = 'C"t~$FwC<IcAyF+[=<}'
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            list_0 = [str_1, str_1, currency_type_0]
            currency_0 = module_2.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_0)
            decimal_1 = currency_0.quantize(decimal_0)
            some_money_0 = module_0.SomeMoney(*list_0)
            money_0 = some_money_0.convert(currency_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
