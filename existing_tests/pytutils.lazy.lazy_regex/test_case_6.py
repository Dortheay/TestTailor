import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            lazy_regex_0 = module_0.LazyRegex()
            str_0 = 'r'
            var_0 = module_0.finditer_public(lazy_regex_0, lazy_regex_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
