import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        int_0 = 1328
        list_0 = [int_0, int_0, int_0]
        float_0 = 4504.2
        set_0 = {int_0, float_0, int_0}
        tuple_0 = (list_0, float_0, float_0, set_0)
        list_1 = [set_0, set_0]
        var_0 = module_0.remove_values(tuple_0, list_1)
        var_1 = module_0.sanitize_keys(tuple_0, list_0)

if __name__ == "__main__":
    unittest.main()
