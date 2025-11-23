import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            money_0 = module_0.Money()
            money_1 = money_0.__sub__(money_0)
            list_0 = [money_0, money_0, money_0, money_0]
            none_price_0 = module_0.NonePrice(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
