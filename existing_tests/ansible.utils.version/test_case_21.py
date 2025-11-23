import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        semantic_version_0 = module_0.SemanticVersion()

if __name__ == "__main__":
    unittest.main()
