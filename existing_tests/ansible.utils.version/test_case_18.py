import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.__le__(semantic_version_0)
            float_0 = 2436.930675
            alpha_0 = module_0._Alpha(float_0)
            bool_0 = True
            numeric_0 = module_0._Numeric(bool_0)
            var_1 = numeric_0.__gt__(alpha_0)
            var_2 = semantic_version_0.__repr__()
            var_3 = numeric_0.__le__(numeric_0)
            set_0 = set()
            float_1 = 954.6153
            numeric_1 = module_0._Numeric(float_1)
            var_4 = numeric_1.__repr__()
            var_5 = semantic_version_0.from_loose_version(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
