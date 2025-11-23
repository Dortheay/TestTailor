import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = -422.69365
            invalid_pattern_0 = module_0.InvalidPattern(float_0)
            var_0 = invalid_pattern_0.__eq__(invalid_pattern_0)
            var_1 = invalid_pattern_0.__unicode__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
