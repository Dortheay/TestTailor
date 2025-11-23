import unittest
import timeout_decorator
import pymonet.lazy as module_0
import builtins as module_1

class Test_Lazy_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = -1230
        list_0 = [int_0, int_0, int_0, int_0]
        bytes_0 = b'\x1f'
        lazy_0 = module_0.Lazy(bytes_0)
        var_0 = lazy_0.bind(list_0)

if __name__ == "__main__":
    unittest.main()
