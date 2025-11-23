import unittest
import timeout_decorator
import ansible.module_utils.common.sys_info as module_0

class Test_Sys_info_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        var_0 = module_0.get_distribution_version()

if __name__ == "__main__":
    unittest.main()
