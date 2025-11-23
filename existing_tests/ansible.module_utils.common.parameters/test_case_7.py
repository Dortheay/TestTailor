import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 81
        str_0 = "V4'@m7"
        var_0 = module_0.sanitize_keys(int_0, str_0, str_0)

if __name__ == "__main__":
    unittest.main()
