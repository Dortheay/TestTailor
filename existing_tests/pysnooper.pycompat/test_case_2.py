import unittest
import timeout_decorator
import datetime as module_0
import pysnooper.pycompat as module_1

class Test_Pycompat_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = 456789
        timedelta_0 = module_0.timedelta()
        var_0 = module_1.timedelta_format(timedelta_0)
        int_4 = 23
        int_5 = 59
        int_6 = 999999
        timedelta_1 = module_0.timedelta()
        var_1 = module_1.timedelta_format(timedelta_1)

if __name__ == "__main__":
    unittest.main()
