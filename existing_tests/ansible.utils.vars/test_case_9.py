import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'a'
        str_1 = 'b'
        int_0 = 1
        int_1 = 2
        int_2 = {str_0: int_0, str_1: int_1}
        str_2 = 'c'
        int_3 = 3
        int_4 = 4
        int_5 = {str_1: int_3, str_2: int_4}
        var_0 = module_0.merge_hash(int_2, int_5)
        int_6 = {str_0: int_0, str_1: int_3}
        int_7 = {str_0: int_6, str_1: int_3}
        str_3 = 'z'
        int_8 = 5
        int_9 = 6
        int_10 = {str_0: int_3, str_2: int_9}
        bool_0 = False
        var_1 = module_0.merge_hash(int_7, int_10, bool_0)
        var_2 = [bool_0, int_1]
        var_3 = {str_0: var_2, str_1: int_3}
        int_11 = [int_3, int_4]
        int_12 = {str_0: int_11, str_2: int_8}
        var_4 = module_0.merge_hash(var_3, int_12, str_2)
        str_4 = 'append'
        var_5 = module_0.merge_hash(var_3, int_12, str_4)
        var_6 = module_0.merge_hash(var_3, int_12, str_3)
        str_5 = 'invalid_option'
        var_7 = module_0.merge_hash(var_3, int_12, str_5)

if __name__ == "__main__":
    unittest.main()
