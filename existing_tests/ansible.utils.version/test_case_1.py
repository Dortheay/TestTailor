import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = "y/+zwK~$l'Y"
            semantic_version_0 = module_0.SemanticVersion()
            alpha_0 = module_0._Alpha(semantic_version_0)
            var_0 = alpha_0.__ne__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
