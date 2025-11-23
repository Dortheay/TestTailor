import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = None
            str_1 = "9';"
            int_0 = -3716
            currency_type_0 = module_2.CurrencyType.METAL
            decimal_0 = module_1.Decimal()
            currency_0 = module_2.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_0)
            bytes_0 = b'\xd4\x8a\xc8\xc8wb\xc5f\xb4\xcdP\x8d\x01$R\x87'
            var_0 = currency_0.__lt__(bytes_0)
            incompatible_currency_error_0 = module_0.IncompatibleCurrencyError(currency_0, currency_0)
            list_0 = []
            str_2 = '.;[ZM/\nAr]ee[Ju7d>'
            str_3 = '^-m'
            dict_0 = {str_2: incompatible_currency_error_0, str_3: currency_type_0, str_3: list_0}
            none_price_0 = module_0.NonePrice()
            money_0 = none_price_0.times(dict_0)
            list_1 = [str_1, str_0, str_0]
            some_money_0 = module_0.SomeMoney(*list_1)
            money_1 = some_money_0.add(money_0)
            bool_0 = money_1.__eq__(str_0)
            dict_1 = {}
            some_money_1 = module_0.SomeMoney(*list_0, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
