import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            str_0 = "'`"
            dict_0 = {str_0: str_0, str_0: str_0}
            int_0 = 2030
            var_0 = module_1.symmetric_difference(dict_0, int_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
