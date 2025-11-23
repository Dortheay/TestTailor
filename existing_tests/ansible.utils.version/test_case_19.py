import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            semantic_version_0 = module_0.SemanticVersion()
            var_0 = semantic_version_0.__le__(semantic_version_0)
            float_0 = 2436.930675
            alpha_0 = module_0._Alpha(float_0)
            bool_0 = True
            numeric_0 = module_0._Numeric(bool_0)
            var_1 = numeric_0.__gt__(alpha_0)
            var_2 = semantic_version_0.__repr__()
            int_0 = 1756
            set_0 = set()
            float_1 = 954.6153
            bool_1 = True
            var_3 = numeric_0.__gt__(bool_1)
            var_4 = alpha_0.__lt__(alpha_0)
            numeric_1 = module_0._Numeric(float_1)
            var_5 = numeric_1.__repr__()
            alpha_1 = module_0._Alpha(set_0)
            numeric_2 = module_0._Numeric(int_0)
            int_1 = -665
            set_1 = set()
            tuple_0 = (int_1, set_0, set_1)
            var_6 = semantic_version_0.from_loose_version(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
