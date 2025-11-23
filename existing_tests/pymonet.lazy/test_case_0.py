import unittest
import timeout_decorator
import pymonet.lazy as module_0

class Test_Lazy_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'f:rXcD[0(D0R-KEd'
            lazy_0 = module_0.Lazy(str_0)
            lazy_1 = module_0.Lazy(lazy_0)
            var_0 = lazy_1.to_either()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
