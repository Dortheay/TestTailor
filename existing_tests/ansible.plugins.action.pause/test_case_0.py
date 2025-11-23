import unittest
import timeout_decorator
import ansible.plugins.action.pause as module_0

class Test_Pause_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -13
        var_0 = module_0.is_interactive(int_0)

if __name__ == "__main__":
    unittest.main()
