import unittest
import timeout_decorator
import pymonet.utils as module_0

class Test_Utils_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = -361
            bytes_0 = b" \xad\x9b\x80n\xa2\xc5\xf8o\x08\xde9ji'"
            var_0 = module_0.curry(int_0, bytes_0)
            float_0 = -2702.8073
            var_1 = module_0.pipe(float_0)
            var_2 = module_0.fn()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
