import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'a'
            str_1 = 'b'
            int_0 = 1
            int_1 = 2
            int_2 = [int_0, int_1]
            int_3 = {str_0: int_0, str_1: int_2}
            str_2 = 'c'
            int_4 = 3
            int_5 = 4
            int_6 = [int_4, int_5]
            int_7 = {str_1: int_6, str_2: int_1}
            bool_0 = False
            str_3 = 'replace'
            var_0 = module_0.merge_hash(int_3, int_7, bool_0, str_3)
            str_4 = 'd'
            int_8 = [int_0, int_1]
            str_5 = 'x'
            str_6 = 'y'
            int_9 = {str_5: int_0, str_6: int_1}
            int_10 = {str_0: int_0, str_1: int_8, str_4: int_9}
            int_11 = [int_4, int_5]
            str_7 = 'z'
            int_12 = {str_6: int_4, str_7: int_5}
            int_13 = {str_1: int_11, str_2: int_1, str_4: int_12}
            bool_1 = True
            str_8 = 'append'
            var_1 = module_0.merge_hash(int_10, int_13, bool_1, str_8)
            bool_2 = True
            str_9 = 'prepend'
            var_2 = module_0.merge_hash(int_10, int_13, bool_2, str_9)
            var_3 = [bool_2, int_1, int_4]
            var_4 = {str_0: bool_2, str_1: var_3}
            int_14 = 5
            int_15 = [int_4, int_5, int_14]
            int_16 = {str_1: int_15}
            bool_3 = True
            str_10 = 'append_rp'
            var_5 = module_0.merge_hash(var_4, int_16, bool_3, str_10)
            bool_4 = True
            str_11 = 'prepend_rp'
            var_6 = module_0.merge_hash(var_4, int_16, bool_4, str_11)
            bool_5 = True
            str_12 = 'keep'
            var_7 = module_0.merge_hash(var_4, int_16, bool_5, str_12)
            var_8 = {}
            var_9 = {}
            str_13 = 'invalid_option'
            var_10 = module_0.merge_hash(var_8, var_9, str_13)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
