import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.from_loose_version(semantic_version_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
