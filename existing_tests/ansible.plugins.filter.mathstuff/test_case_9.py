import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            str_0 = 'p'
            str_1 = 'kinit_mode'
            str_2 = ''
            dict_0 = {str_1: bool_0, str_2: str_2, str_1: str_1}
            var_0 = module_1.unique(bool_0, str_0, str_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
