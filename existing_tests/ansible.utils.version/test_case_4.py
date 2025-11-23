import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = False
            float_0 = 2301.0
            numeric_0 = module_0._Numeric(float_0)
            alpha_0 = module_0._Alpha(numeric_0)
            var_0 = alpha_0.__lt__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
