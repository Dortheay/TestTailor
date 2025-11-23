import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_57(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        int_0 = 3242
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        decimal_0 = module_2.Decimal()
        str_1 = ''
        str_2 = 'C"t~$FwC<IcAyF+[=<}'
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        currency_0 = module_1.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_0)
        decimal_1 = currency_0.quantize(decimal_0)
        money_1 = money_0.add(money_0)
        var_0 = money_1.__round__()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.round()
        price_1 = price_0.__sub__(price_0)

if __name__ == "__main__":
    unittest.main()
