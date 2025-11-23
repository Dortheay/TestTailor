import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = 1619.321
        lazy_regex_0 = module_0.LazyRegex()
        invalid_pattern_0 = module_0.InvalidPattern(lazy_regex_0)
        var_0 = invalid_pattern_0.__eq__(float_0)

if __name__ == "__main__":
    unittest.main()
