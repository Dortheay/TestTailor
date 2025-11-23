import unittest
import timeout_decorator
import ansible.plugins.action.pause as module_0

class Test_Pause_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = None
        var_1 = module_0.is_interactive(var_0)
        int_0 = -13
        var_2 = module_0.is_interactive(int_0)

if __name__ == "__main__":
    unittest.main()
