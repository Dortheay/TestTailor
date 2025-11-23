import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 3217
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        decimal_0 = module_2.Decimal()
        none_price_0 = module_0.NonePrice()
        bool_0 = none_price_0.as_boolean()
        str_1 = '3C$bqy}h'
        str_2 = 'C"t~$FwC<IcAyF+[=<}'
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        bool_1 = none_money_0.as_boolean()
        list_0 = [str_0, str_0, currency_type_0]
        int_1 = -1891
        currency_0 = module_1.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
        decimal_1 = currency_0.quantize(decimal_0)
        money_0 = none_money_0.with_ccy(currency_0)
        some_money_0 = module_0.SomeMoney(*list_0)
        bool_2 = some_money_0.gte(money_0)
        money_1 = money_0.abs()
        var_0 = money_1.__round__()

if __name__ == "__main__":
    unittest.main()
