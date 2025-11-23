import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -2211
        lazy_0 = module_0.Lazy(int_0)
        str_0 = lazy_0.__str__()

if __name__ == "__main__":
    unittest.main()
