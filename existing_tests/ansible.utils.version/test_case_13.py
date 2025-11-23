import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.__le__(semantic_version_0)
            var_1 = semantic_version_0.__repr__()
            var_2 = semantic_version_0.from_loose_version(semantic_version_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
