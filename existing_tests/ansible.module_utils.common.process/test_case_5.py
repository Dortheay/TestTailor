import unittest
import timeout_decorator
import ansible.module_utils.common.process as module_0

class Test_Process_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = None
            str_0 = ''
            str_1 = 'N\x0b3g\rB\n('
            var_0 = module_0.get_bin_path(str_0, int_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
