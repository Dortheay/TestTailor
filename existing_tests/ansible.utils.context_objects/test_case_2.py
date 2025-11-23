import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'key&'
        str_1 = 'key3'
        str_2 = ''
        str_3 = {str_1: str_1}
        str_4 = {str_0: str_2, str_1: str_3}
        c_l_i_args_0 = module_0.CLIArgs(str_4)
        var_0 = c_l_i_args_0[str_1]

if __name__ == "__main__":
    unittest.main()
