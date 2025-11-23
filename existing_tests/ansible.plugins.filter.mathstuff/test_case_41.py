import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_42(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            str_0 = 'P{vO4'
            int_0 = -2410
            set_0 = {str_0, str_0, int_0}
            var_0 = module_1.symmetric_difference(int_0, set_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
