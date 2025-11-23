import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_31(self):
        try:
            int_0 = 10
            var_0 = module_1.logarithm(int_0)
            int_1 = 100
            var_1 = module_1.logarithm(int_1, int_0)
            int_2 = 16
            int_3 = 2
            var_2 = module_1.logarithm(int_2, int_3)
            str_0 = 'invalid'
            int_4 = 10
            var_3 = module_1.logarithm(str_0, int_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
