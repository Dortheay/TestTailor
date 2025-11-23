import unittest
import timeout_decorator
import ansible.plugins.action.fail as module_0

class Test_Fail_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = 1816.4879
        int_0 = 2098
        str_0 = '5"N $Sibfg\n<pe'
        action_module_0 = module_0.ActionModule(str_0, float_0, int_0, float_0, str_0, str_0)

if __name__ == "__main__":
    unittest.main()
