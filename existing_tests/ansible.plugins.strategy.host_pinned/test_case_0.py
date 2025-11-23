import unittest
import timeout_decorator
import ansible.plugins.strategy.host_pinned as module_0

class Test_Host_pinned_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'D"#hdZYd8@_>\x0blseV;Y'
            strategy_module_0 = module_0.StrategyModule(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
