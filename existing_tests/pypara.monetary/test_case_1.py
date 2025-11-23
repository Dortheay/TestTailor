import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            currency_0 = None
            none_price_0 = module_0.NonePrice()
            price_0 = none_price_0.abs()
            incompatible_currency_error_0 = module_0.IncompatibleCurrencyError(currency_0, currency_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
