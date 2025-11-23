import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_48(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = 3242
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        decimal_0 = module_2.Decimal()
        str_1 = ''
        str_2 = 'C"t~$FwC<IcAyF+[=<}'
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        int_1 = 1317
        currency_0 = module_1.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
        decimal_1 = currency_0.quantize(decimal_0)
        money_1 = none_money_0.negative()
        money_2 = money_0.abs()
        var_0 = money_2.__round__()
        bool_0 = none_money_0.lt(money_2)
        bool_1 = money_0.as_boolean()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.round()

if __name__ == "__main__":
    unittest.main()
