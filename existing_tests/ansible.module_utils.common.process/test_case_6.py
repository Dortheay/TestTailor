import unittest
import timeout_decorator
import ansible.module_utils.common.process as module_0

class Test_Process_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'test'
        var_0 = module_0.get_bin_path(str_0)

if __name__ == "__main__":
    unittest.main()
