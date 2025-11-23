import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = ''
        none_money_0 = module_0.NoneMoney()
        money_0 = none_money_0.scalar_add(str_0)
        monetary_operation_exception_0 = module_0.MonetaryOperationException()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.multiply(monetary_operation_exception_0)
        float_0 = 680.5064
        money_1 = money_0.__mul__(float_0)
        money_2 = none_money_0.positive()
        var_0 = price_0.__round__()
        money_3 = money_0.abs()
        var_1 = money_3.__round__()
        price_1 = none_price_0.round()
        money_4 = money_0.round()
        price_2 = none_price_0.negative()

if __name__ == "__main__":
    unittest.main()
