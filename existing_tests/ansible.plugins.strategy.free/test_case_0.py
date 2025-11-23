import unittest
import timeout_decorator
import ansible.plugins.strategy.free as module_0

class Test_Free_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = ()
            strategy_module_0 = module_0.StrategyModule(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
