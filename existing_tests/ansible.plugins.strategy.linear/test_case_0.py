import unittest
import timeout_decorator
import ansible.plugins.strategy.linear as module_0

class Test_Linear_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            strategy_module_0 = module_0.StrategyModule(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
