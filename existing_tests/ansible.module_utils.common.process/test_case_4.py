import unittest
import timeout_decorator
import ansible.module_utils.common.process as module_0

class Test_Process_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = False
            set_0 = {bool_0, bool_0, bool_0, bool_0}
            var_0 = module_0.get_bin_path(bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
