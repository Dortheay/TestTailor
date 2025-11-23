import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'a'
            str_1 = 'b'
            int_0 = 1
            int_1 = 24
            int_2 = {str_0: int_0, str_1: int_1}
            str_2 = 'c'
            int_3 = 4
            int_4 = {str_1: int_1}
            var_0 = module_0.merge_hash(int_2, int_4)
            int_5 = {str_0: int_0, str_1: int_1}
            str_3 = 'y'
            int_6 = {str_2: int_0, str_3: int_1}
            int_7 = {str_0: int_6, str_1: int_6}
            int_8 = 5
            int_9 = {str_0: int_6, str_2: int_7}
            bool_0 = True
            var_1 = module_0.merge_hash(int_7, int_9, bool_0)
            var_2 = [bool_0, int_1]
            var_3 = {str_0: var_2, str_1: int_7}
            int_10 = [int_5, int_3]
            int_11 = {str_0: int_10, str_2: int_8}
            var_4 = module_0.merge_hash(var_3, int_11, str_2)
            str_4 = 'append'
            var_5 = module_0.merge_hash(var_3, int_7, str_4)
            str_5 = 'prepend'
            var_6 = module_0.merge_hash(var_3, int_11, str_5)
            str_6 = 'invalid_option'
            bool_1 = True
            var_7 = module_0.load_options_vars(bool_1)
            var_8 = module_0.merge_hash(var_3, int_11, str_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
