import unittest
import timeout_decorator
import pysnooper.pycompat as module_0

class Test_Pycompat_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            complex_0 = None
            var_0 = module_0.timedelta_parse(complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
