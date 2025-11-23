import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            list_0 = None
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.__ne__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
