import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        float_0 = 2436.930675
        alpha_0 = module_0._Alpha(float_0)
        bool_0 = True
        numeric_0 = module_0._Numeric(bool_0)
        var_0 = numeric_0.__gt__(alpha_0)
        float_1 = 954.6153
        numeric_1 = module_0._Numeric(float_1)
        var_1 = numeric_1.__repr__()

if __name__ == "__main__":
    unittest.main()
