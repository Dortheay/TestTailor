import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'key1'
        str_1 = 'key2'
        str_2 = 'key3'
        str_3 = 'value1'
        str_4 = 'item1'
        str_5 = 'item2'
        str_6 = [str_4, str_5]
        str_7 = 'sub_key'
        str_8 = {str_7: str_1}
        str_9 = {str_0: str_3, str_1: str_6, str_2: str_8}
        c_l_i_args_0 = module_0.CLIArgs(str_9)
        var_0 = c_l_i_args_0[str_2]

if __name__ == "__main__":
    unittest.main()
