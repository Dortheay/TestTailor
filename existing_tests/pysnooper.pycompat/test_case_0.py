import unittest
import timeout_decorator
import pysnooper.pycompat as module_0

class Test_Pycompat_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'D\xb8\x81/\x9fm\r\xc1'
            var_0 = module_0.timedelta_format(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
