import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        loose_version_0 = module_0.LooseVersion()

if __name__ == "__main__":
    unittest.main()
