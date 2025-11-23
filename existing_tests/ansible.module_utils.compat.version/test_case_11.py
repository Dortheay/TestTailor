import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '2mz'
        loose_version_0 = module_0.LooseVersion()
        var_0 = loose_version_0.parse(str_0)

if __name__ == "__main__":
    unittest.main()
