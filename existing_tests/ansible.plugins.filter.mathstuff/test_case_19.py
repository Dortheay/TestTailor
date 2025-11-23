import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'AIPO'
            filter_module_0 = module_1.FilterModule()
            var_0 = module_1.inversepower(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
