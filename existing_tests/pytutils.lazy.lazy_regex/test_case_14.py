import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        var_0 = module_0.lazy_compile()

if __name__ == "__main__":
    unittest.main()
