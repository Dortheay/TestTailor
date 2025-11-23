import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        float_0 = 4504.2
        int_0 = -1701
        set_0 = {int_0, float_0, int_0}
        int_1 = -3013
        var_0 = module_0.remove_values(int_1, set_0)

if __name__ == "__main__":
    unittest.main()
