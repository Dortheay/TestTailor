import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            date_time_format_0 = module_0.DateTimeFormat()
            str_0 = '2023-10-30T14:45:00Z'
            datetime_0 = date_time_format_0.validate(str_0)
            str_1 = '2023-10-30T14:45:00+02:00'
            datetime_1 = date_time_format_0.validate(str_1)
            int_0 = 2
            timedelta_0 = module_2.timedelta()
            str_2 = '2023-10-30T14:45:00-05:00'
            datetime_2 = date_time_format_0.validate(str_2)
            int_1 = -5
            timedelta_1 = module_2.timedelta()
            str_3 = '2023-10-30 14:45'
            datetime_3 = date_time_format_0.validate(str_3)
            str_4 = 'invalid-datetime'
            datetime_4 = date_time_format_0.validate(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
