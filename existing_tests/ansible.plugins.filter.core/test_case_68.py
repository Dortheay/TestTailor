import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_69(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()

if __name__ == "__main__":
    unittest.main()
