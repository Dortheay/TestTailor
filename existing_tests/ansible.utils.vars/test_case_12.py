import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'key2'
            str_1 = 'value1'
            str_2 = 'value2'
            str_3 = {str_1: str_1, str_0: str_2}
            str_4 = 'key3'
            str_5 = 'new_value2'
            str_6 = 'value3'
            str_7 = {str_0: str_5, str_4: str_6}
            var_0 = module_0.combine_vars(str_3, str_7)
            var_1 = module_0.combine_vars(str_3, str_7)
            var_2 = module_0.merge_hash(str_3, str_7)
            str_8 = [str_1, str_2]
            var_3 = module_0.combine_vars(str_8, str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
