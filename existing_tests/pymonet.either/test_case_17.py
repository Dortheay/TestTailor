import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = -305
            bytes_0 = b'\xaf'
            right_0 = module_0.Right(bytes_0)
            var_0 = right_0.bind(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
