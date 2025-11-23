import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            loose_version_0 = module_0.LooseVersion()
            strict_version_0 = module_0.StrictVersion()
            var_0 = strict_version_0.__str__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
