import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_46(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        none_price_0 = module_0.NonePrice()
        list_0 = []
        str_0 = '=dhh]xm0'
        str_1 = "GtJ(J'm\nV.Fq+Q"
        int_0 = -3978
        currency_type_0 = module_1.CurrencyType.CRYPTO
        decimal_0 = module_2.Decimal()
        currency_0 = module_1.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_0)
        price_0 = none_price_0.convert(currency_0)
        price_1 = price_0.divide(list_0)
        price_2 = price_1.__pos__()
        price_3 = none_price_0.scalar_subtract(price_2)

if __name__ == "__main__":
    unittest.main()
