import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = 1.5
        str_0 = '0'
        numeric_0 = module_0._Numeric(str_0)
        var_0 = numeric_0.__ne__(float_0)
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)

if __name__ == "__main__":
    unittest.main()
