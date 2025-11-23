import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            some_money_0 = module_0.SomeMoney()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
