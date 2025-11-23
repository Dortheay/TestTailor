import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -583
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        c_l_i_args_0 = module_0.CLIArgs(dict_0)

if __name__ == "__main__":
    unittest.main()
