import unittest
import timeout_decorator
import ansible.module_utils.common.process as module_0

class Test_Process_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'kfByL_s\t<'
            var_0 = module_0.get_bin_path(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
