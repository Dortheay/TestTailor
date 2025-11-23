import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            var_0 = None
            none_price_0 = module_0.NonePrice()
            price_0 = none_price_0.divide(var_0)
            bool_0 = price_0.__bool__()
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.positive()
            money_1 = money_0.__abs__()
            str_0 = 'Turkish Lira'
            int_0 = 29
            currency_type_0 = module_2.CurrencyType.CRYPTO
            decimal_0 = None
            currency_0 = module_2.Currency(str_0, str_0, int_0, currency_type_0, decimal_0, int_0)
            money_2 = money_1.convert(currency_0)
            float_0 = price_0.as_float()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
