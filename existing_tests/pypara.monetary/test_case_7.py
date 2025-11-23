import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = 3242
            str_0 = ''
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.scalar_add(str_0)
            decimal_0 = module_1.Decimal()
            monetary_operation_exception_0 = module_0.MonetaryOperationException()
            none_price_0 = module_0.NonePrice()
            price_0 = none_price_0.abs()
            str_1 = '3C$bqy}h'
            str_2 = 'C"t~$FwC<IcAyF+[=<}'
            currency_type_0 = module_2.CurrencyType.ALTERNATIVE
            int_1 = -1891
            int_2 = -1099
            currency_0 = module_2.Currency(str_1, str_2, int_1, currency_type_0, decimal_0, int_2)
            price_1 = price_0.with_ccy(currency_0)
            var_0 = price_0.__round__()
            currency_1 = module_2.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
            decimal_1 = None
            decimal_2 = currency_1.quantize(decimal_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
