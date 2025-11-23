import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            semantic_version_0 = module_0.SemanticVersion()
            alpha_0 = module_0._Alpha(semantic_version_0)
            bytes_0 = None
            var_0 = semantic_version_0.from_loose_version(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
