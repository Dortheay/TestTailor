import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            none_money_0 = module_0.NoneMoney()
            money_0 = none_money_0.negative()
            list_0 = []
            str_0 = 'B85sx'
            str_1 = '\n        Initializes the root accounts buffer.\n        '
            dict_0 = {str_0: list_0, str_1: list_0}
            some_money_0 = module_0.SomeMoney(*list_0, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
