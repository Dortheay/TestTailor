import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__eq__(alpha_0)

if __name__ == "__main__":
    unittest.main()
