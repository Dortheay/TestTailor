import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'list'
        str_1 = 'nested_dict'
        str_2 = 'set'
        int_0 = 3
        int_1 = [int_0, int_0, int_0]
        str_3 = {str_2: str_1}
        int_2 = 4
        int_3 = 10
        int_4 = {int_2, int_2, int_3}
        var_0 = {str_2: str_2, str_0: int_1, str_1: str_3, str_2: int_4}
        c_l_i_args_0 = module_0.CLIArgs(var_0)
        var_1 = frozenset(int_4)

if __name__ == "__main__":
    unittest.main()
