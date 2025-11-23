import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = 'gg \\ '
            str_1 = ''
            dict_0 = {str_0: str_0, str_0: str_1, str_1: str_0}
            var_0 = module_1.rekey_on_member(dict_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
