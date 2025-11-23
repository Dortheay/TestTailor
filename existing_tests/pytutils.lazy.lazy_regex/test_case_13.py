import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        var_0 = module_0.reset_compile()
        lazy_regex_0 = module_0.LazyRegex()
        var_1 = lazy_regex_0.__getstate__()

if __name__ == "__main__":
    unittest.main()
