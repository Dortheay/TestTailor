import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            str_0 = '1.2.3-alpha.1+build.123'
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.parse(str_0)
            str_1 = 'alpha'
            alpha_0 = module_0._Alpha(str_1)
            int_0 = 1
            numeric_0 = module_0._Numeric(int_0)
            str_2 = 'build'
            alpha_1 = module_0._Alpha(str_2)
            int_1 = 123
            numeric_1 = module_0._Numeric(int_1)
            str_3 = '0.9.0'
            semantic_version_1 = module_0.SemanticVersion()
            var_1 = semantic_version_1.parse(str_3)
            str_4 = 'invalid.version'
            semantic_version_2 = module_0.SemanticVersion()
            var_2 = semantic_version_2.parse(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
