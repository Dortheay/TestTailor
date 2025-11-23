import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 730
            bytes_0 = b'j'
            var_0 = module_0.combine_vars(int_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
