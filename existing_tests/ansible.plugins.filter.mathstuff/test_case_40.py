import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_32(self):
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
            str_4 = 'Charlie'
            var_2 = {str_0: int_2, str_1: str_4}
            var_3 = [var_0, var_1, var_2]
            str_5 = 'id'
            var_4 = {str_0: int_0, str_1: str_2}
            var_5 = module_1.rekey_on_member(var_3, str_5)
            var_6 = [var_4, var_4]
            str_6 = 'overwrite'
            var_7 = module_1.rekey_on_member(var_6, str_5, str_6)
            str_7 = 'error'
            var_8 = module_1.rekey_on_member(var_6, str_5, str_7)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
