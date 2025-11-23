import unittest
import timeout_decorator
import ansible.plugins.action.set_stats as module_0

class Test_Set_stats_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = None
        action_module_0 = module_0.ActionModule(var_0, var_0, var_0, var_0, var_0, var_0)

if __name__ == "__main__":
    unittest.main()
