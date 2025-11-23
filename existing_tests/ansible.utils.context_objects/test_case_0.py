import unittest
import timeout_decorator
import ansible.utils.context_objects as module_0

class Test_Context_objects_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '"]-?/z=_'
            global_c_l_i_args_0 = module_0.GlobalCLIArgs(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
