import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            version_0 = module_0.Version()
            str_0 = '/usr/local/bin'
            loose_version_0 = module_0.LooseVersion(str_0)
            strict_version_0 = module_0.StrictVersion()
            var_0 = version_0.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
