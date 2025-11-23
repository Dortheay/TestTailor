import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '\\d+'
            str_1 = (str_0,)
            var_0 = {}
            lazy_regex_0 = module_0.LazyRegex(str_1, var_0)
            var_1 = lazy_regex_0.match
            var_2 = callable(var_1)
            int_0 = 856
            var_3 = lazy_regex_0.__getattr__(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
