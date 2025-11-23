import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            var_0 = module_1.logarithm(bool_0)
            bytes_0 = b')k=;#\xdaW'
            bool_1 = True
            filter_module_0 = module_1.FilterModule()
            var_1 = module_1.intersect(bytes_0, bool_1, filter_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
