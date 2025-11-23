import unittest
import timeout_decorator
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

class Test_Monetary_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            float_0 = 2833.0
            list_0 = [float_0, float_0, float_0]
            some_money_0 = module_0.SomeMoney(*list_0)
            some_money_1 = module_0.SomeMoney(*list_0)
            money_0 = some_money_1.scalar_add(some_money_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
