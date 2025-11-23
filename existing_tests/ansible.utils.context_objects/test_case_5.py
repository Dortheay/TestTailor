import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'string_key'
        str_1 = 'list_key'
        str_2 = 'set_key'
        str_3 = 'value'
        int_0 = 42
        int_1 = 1
        int_2 = 2
        int_3 = 3
        int_4 = [int_1, int_2, int_3]
        str_4 = 'nested_key'
        str_5 = 'nested_value'
        str_6 = {str_4: str_5}
        str_7 = 'a'
        str_8 = 'b'
        str_9 = 'c'
        str_10 = {str_7, str_8, str_9}
        var_0 = {str_0: str_3, str_7: int_0, str_1: int_4, str_5: str_6, str_2: str_10}
        c_l_i_args_0 = module_0.CLIArgs(var_0)
        str_11 = {str_7, str_8, str_9}
        var_1 = frozenset(str_11)

if __name__ == "__main__":
    unittest.main()
