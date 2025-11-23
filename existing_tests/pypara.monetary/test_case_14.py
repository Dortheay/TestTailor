import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            int_0 = -1562
            list_0 = [int_0, int_0, int_0]
            money_0 = None
            some_money_0 = module_0.SomeMoney(*list_0)
            bool_0 = some_money_0.lt(money_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
