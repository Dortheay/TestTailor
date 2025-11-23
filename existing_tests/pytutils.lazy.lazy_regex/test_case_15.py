import unittest
import timeout_decorator
import pytutils.lazy.lazy_regex as module_0

class Test_Lazy_regex_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        var_0 = module_0.install_lazy_compile()

if __name__ == "__main__":
    unittest.main()
