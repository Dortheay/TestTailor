import unittest
import timeout_decorator
import ansible.plugins.strategy.debug as module_0

class Test_Debug_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 4206
            strategy_module_0 = module_0.StrategyModule(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
