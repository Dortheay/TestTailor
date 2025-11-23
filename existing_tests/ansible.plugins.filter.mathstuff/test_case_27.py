import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            filter_module_0 = module_1.FilterModule()
            str_0 = '\x0bO*(fqX'
            complex_0 = None
            var_0 = module_1.inversepower(str_0, complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
