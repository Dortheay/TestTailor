import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_55(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        int_0 = 3234
        none_money_0 = module_0.NoneMoney()
        decimal_0 = module_2.Decimal()
        monetary_operation_exception_0 = module_0.MonetaryOperationException()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.negative()
        price_1 = price_0.__neg__()
        price_2 = price_1.__neg__()
        str_0 = '3C$bqy}h'
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        int_1 = -1891
        money_0 = none_money_0.positive()
        var_0 = price_0.__round__()
        currency_0 = module_1.Currency(str_0, str_0, int_0, currency_type_0, decimal_0, int_1)
        decimal_1 = currency_0.quantize(decimal_0)
        price_3 = price_0.with_qty(decimal_0)

if __name__ == "__main__":
    unittest.main()
