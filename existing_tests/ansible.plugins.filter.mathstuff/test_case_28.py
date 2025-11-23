import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = 'id'
            str_1 = 'name'
            int_0 = 1
            str_2 = 'Alice'
            var_0 = {str_0: int_0, str_1: str_2}
            int_1 = 2
            str_3 = 'Bob'
            var_1 = {str_0: int_1, str_1: str_3}
            int_2 = 3
            var_2 = {str_0: int_2, str_1: str_0}
            var_3 = [var_0, var_1, var_2]
            dict_0 = {str_3: int_1, str_2: int_1, str_1: var_2}
            str_4 = '$x'
            var_4 = module_1.min(dict_0, str_4)
            str_5 = 'id'
            var_5 = {str_0: int_0, str_1: str_2}
            var_6 = module_1.rekey_on_member(var_3, str_5)
            var_7 = [var_5, var_5]
            var_8 = module_1.rekey_on_member(var_7, str_5, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
