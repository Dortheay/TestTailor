import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 1330
        set_0 = {int_0}
        str_0 = ".Ji2Isz*C=r&')"
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.map(set_0)

if __name__ == "__main__":
    unittest.main()
