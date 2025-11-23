import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_63(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        int_0 = 3242
        str_0 = 'h'
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        decimal_0 = module_2.Decimal()
        monetary_operation_exception_0 = module_0.MonetaryOperationException()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.multiply(monetary_operation_exception_0)
        str_1 = '3C$bqy}h'
        str_2 = 'C"tw$FwC<qcAyF+[=<}'
        currency_type_0 = module_1.CurrencyType.ALTERNATIVE
        int_1 = -1891
        bool_0 = price_0.gt(price_0)
        var_0 = price_0.__round__()
        currency_0 = module_1.Currency(str_1, str_2, int_0, currency_type_0, decimal_0, int_1)
        decimal_1 = currency_0.quantize(decimal_0)
        money_1 = money_0.with_qty(decimal_1)
        money_2 = money_0.abs()
        var_1 = money_2.__round__()

if __name__ == "__main__":
    unittest.main()
