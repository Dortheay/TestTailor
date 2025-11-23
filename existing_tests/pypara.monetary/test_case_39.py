import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_39(self):
        try:
            int_0 = 3217
            some_price_0 = None
            none_price_0 = module_0.NonePrice()
            money_0 = none_price_0.times(some_price_0)
            str_0 = ''
            none_money_0 = module_0.NoneMoney()
            money_1 = none_money_0.scalar_add(str_0)
            decimal_0 = module_1.Decimal()
            none_price_1 = module_0.NonePrice()
            bool_0 = none_price_1.as_boolean()
            str_1 = '3C$\nbqylh'
            str_2 = 'C"t~$FwC<IcAyF+[=<}'
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            list_0 = [str_0, str_0, currency_type_0]
            currency_0 = module_2.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_0)
            bool_1 = money_1.__bool__()
            decimal_1 = currency_0.quantize(decimal_0)
            money_2 = money_1.with_qty(decimal_1)
            some_money_0 = module_0.SomeMoney(*list_0)
            date_0 = None
            price_0 = none_price_1.with_dov(date_0)
            bool_2 = some_money_0.gte(money_2)
            money_3 = money_1.abs()
            money_4 = some_money_0.add(money_2)
            var_0 = money_3.__round__()
            money_5 = some_money_0.convert(currency_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
