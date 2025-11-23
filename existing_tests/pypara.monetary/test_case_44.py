import unittest
import timeout_decorator
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

class Test_Monetary_45(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        money_0 = None
        bool_0 = True
        list_0 = [bool_0]
        none_money_0 = module_0.NoneMoney()
        money_1 = none_money_0.scalar_add(list_0)
        bool_1 = money_1.__gt__(money_0)

if __name__ == "__main__":
    unittest.main()
