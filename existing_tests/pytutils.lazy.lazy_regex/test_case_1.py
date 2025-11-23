import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -1795.7844565748203
            invalid_pattern_0 = module_0.InvalidPattern(float_0)
            var_0 = invalid_pattern_0.__unicode__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
