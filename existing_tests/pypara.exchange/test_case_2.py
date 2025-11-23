import unittest
import timeout_decorator
import pypara.currencies as module_0
import decimal as module_1
import pypara.exchange as module_2

class Test_Exchange_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = "fDq3 8=j(|xu'`5\\M;`"
        int_0 = 2121
        currency_type_0 = module_0.CurrencyType.METAL
        decimal_0 = module_1.Decimal()
        currency_0 = module_0.Currency(str_0, str_0, int_0, currency_type_0, decimal_0, int_0)
        date_0 = None
        f_x_rate_lookup_error_0 = module_2.FXRateLookupError(currency_0, currency_0, date_0)

if __name__ == "__main__":
    unittest.main()
