import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_56(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        monetary_operation_exception_0 = module_0.MonetaryOperationException()
        none_price_0 = module_0.NonePrice()
        price_0 = none_price_0.multiply(monetary_operation_exception_0)
        var_0 = price_0.__round__()
        price_1 = none_price_0.negative()

if __name__ == "__main__":
    unittest.main()
