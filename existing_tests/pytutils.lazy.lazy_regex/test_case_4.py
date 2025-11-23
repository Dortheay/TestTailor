import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = True
            lazy_regex_0 = module_0.LazyRegex()
            var_0 = lazy_regex_0.__setstate__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
