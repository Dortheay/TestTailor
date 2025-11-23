import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        lazy_regex_0 = module_0.LazyRegex()

if __name__ == "__main__":
    unittest.main()
