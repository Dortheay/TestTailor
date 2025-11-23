import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_72(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        filter_module_0 = None
        bytes_0 = None
        var_0 = module_0.ternary(filter_module_0, filter_module_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
