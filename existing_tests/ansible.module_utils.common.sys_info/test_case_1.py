import unittest
import timeout_decorator
import ansible.module_utils.common.sys_info as module_0

class Test_Sys_info_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        var_0 = module_0.get_distribution()

if __name__ == "__main__":
    unittest.main()
