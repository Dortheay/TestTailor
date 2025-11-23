import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_60(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        int_0 = 3242
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        str_1 = 'r!Z\\Agqb:j@5ZnO_aU'
        str_2 = '~Z0.nl;mvoK'
        currency_type_0 = module_1.CurrencyType.CRYPTO
        bool_0 = money_0.is_equal(int_0)
        decimal_0 = None
        int_1 = None
        currency_0 = module_1.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
        bool_1 = False
        money_1 = none_money_0.convert(currency_0, bool_1)
        decimal_1 = module_2.Decimal()
        str_3 = 'im+*7c)1zY9z_ @\t(XXN'
        str_4 = 'C"t~$FwC<IcAyF+[=<}'
        bool_2 = money_0.__le__(money_0)
        currency_type_1 = module_1.CurrencyType.CRYPTO
        int_2 = 1304
        currency_1 = module_1.Currency(str_3, str_4, int_0, currency_type_1, decimal_1, int_2)
        decimal_2 = currency_1.quantize(decimal_1)
        money_2 = none_money_0.negative()
        money_3 = money_2.round()
        var_0 = money_3.__round__()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.round()
        price_1 = none_price_0.negative()

if __name__ == "__main__":
    unittest.main()
