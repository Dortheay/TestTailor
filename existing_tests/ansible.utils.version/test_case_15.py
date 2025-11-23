import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = 'lWX\x0cwJ'
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.__ge__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
