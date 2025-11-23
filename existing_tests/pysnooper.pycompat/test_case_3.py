import unittest
import timeout_decorator
import datetime as module_0
import pysnooper.pycompat as module_1

class Test_Pycompat_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '01:02:03.000004'
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = 4
        timedelta_0 = module_0.timedelta()
        var_0 = module_1.timedelta_parse(str_0)
        str_1 = '00:00:00.000000'
        timedelta_1 = module_0.timedelta()
        var_1 = module_1.timedelta_parse(str_1)
        str_2 = '00:00:00.999999'
        int_4 = 999999
        timedelta_2 = module_0.timedelta()
        var_2 = module_1.timedelta_parse(str_2)
        str_3 = '23:59:59.999999'
        int_5 = 23
        int_6 = 59
        timedelta_3 = module_0.timedelta()
        var_3 = module_1.timedelta_parse(str_3)
        str_4 = '25:00:00.000000'
        var_4 = module_1.timedelta_parse(str_4)

if __name__ == "__main__":
    unittest.main()
