import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'list'
        str_1 = 'nested_dict'
        str_2 = 'set'
        str_3 = 'p<JF"v&/!K8(:-O'
        int_0 = 3
        str_4 = {str_3: str_0}
        int_1 = 4
        int_2 = 6
        int_3 = {int_1, int_1, int_2}
        var_0 = {str_2: str_3, str_0: int_0, str_1: str_4, str_2: int_3}
        c_l_i_args_0 = module_0.CLIArgs(var_0)
        var_1 = frozenset(int_3)

if __name__ == "__main__":
    unittest.main()
