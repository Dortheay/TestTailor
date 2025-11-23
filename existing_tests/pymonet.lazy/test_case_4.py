import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = -2222
        lazy_0 = module_0.Lazy(int_0)

if __name__ == "__main__":
    unittest.main()
