import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'a'
        int_0 = 1
        int_1 = 2
        int_2 = {str_0: int_0, str_0: int_1}
        str_1 = 'c'
        int_3 = 4
        int_4 = {str_1: int_1, str_1: int_3}
        var_0 = module_0.merge_hash(int_2, int_4)
        str_2 = 'x'
        str_3 = 'y'
        int_5 = {str_2: int_0, str_3: int_1}
        int_6 = {str_0: int_5, str_3: int_5}
        int_7 = 5
        int_8 = 11
        int_9 = {str_0: int_5, str_1: int_8}
        bool_0 = True
        var_1 = module_0.merge_hash(int_6, int_9, bool_0)
        var_2 = [bool_0, int_1]
        var_3 = {str_0: var_2, str_1: int_6}
        int_10 = [int_8, int_3]
        int_11 = {str_0: int_10, str_1: int_7}
        var_4 = module_0.merge_hash(var_3, int_11, str_1)
        str_4 = 'append'
        var_5 = module_0.merge_hash(var_3, int_11, str_4)
        str_5 = 'prepend'
        var_6 = module_0.merge_hash(var_3, int_11, str_5)

if __name__ == "__main__":
    unittest.main()
