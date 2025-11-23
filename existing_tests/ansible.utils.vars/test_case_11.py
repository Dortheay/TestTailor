import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '.|)/3Cb'
            bytes_0 = None
            bool_0 = True
            var_0 = module_0.combine_vars(str_0, bytes_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
