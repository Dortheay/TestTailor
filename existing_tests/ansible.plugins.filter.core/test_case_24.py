import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            list_0 = []
            filter_module_0 = module_0.FilterModule()
            var_0 = module_0.rand(filter_module_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
