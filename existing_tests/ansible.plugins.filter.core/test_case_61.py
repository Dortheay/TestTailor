import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_62(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        filter_module_0 = module_0.FilterModule()
        int_0 = 3002
        var_0 = module_0.randomize_list(int_0)

if __name__ == "__main__":
    unittest.main()
