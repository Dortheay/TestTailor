import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_52(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = 0.001
        var_0 = module_0.to_nice_json(float_0)
        filter_module_0 = module_0.FilterModule()
        int_0 = 3002
        var_1 = module_0.randomize_list(int_0)

if __name__ == "__main__":
    unittest.main()
