import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = -1796.272755
        invalid_pattern_0 = module_0.InvalidPattern(float_0)

if __name__ == "__main__":
    unittest.main()
