import unittest
import timeout_decorator
import ansible.module_utils.common.process as module_0

class Test_Process_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 978
            var_0 = module_0.get_bin_path(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
