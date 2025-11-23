import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            price_0 = None
            str_0 = '\n@'
            list_0 = [str_0, str_0, str_0]
            some_price_0 = module_0.SomePrice(*list_0)
            money_0 = some_price_0.times(price_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
