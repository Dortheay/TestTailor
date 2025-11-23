import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            filter_module_0 = module_0.FilterModule()
            var_0 = filter_module_0.filters()
            set_0 = None
            var_1 = module_0.to_datetime(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
