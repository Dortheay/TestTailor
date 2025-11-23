import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            loose_version_0 = module_0.LooseVersion()
            var_0 = loose_version_0.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
