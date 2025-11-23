import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_34(self):
        try:
            money_0 = module_0.Money()
            decimal_0 = module_1.Decimal()
            currency_type_0 = module_2.CurrencyType.CRYPTO
            money_1 = money_0.__floordiv__(currency_type_0)
            some_price_0 = module_0.SomePrice()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
