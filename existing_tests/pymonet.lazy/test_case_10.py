import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '<uftF_-'
        float_0 = 1302.0
        lazy_0 = module_0.Lazy(float_0)
        var_0 = lazy_0.map(str_0)
        lazy_1 = module_0.Lazy(var_0)
        var_1 = lazy_1.to_try()

if __name__ == "__main__":
    unittest.main()
