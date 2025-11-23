import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            date_time_format_0 = module_0.DateTimeFormat()
            str_0 = '2023-03-15T14:30:45.123456Z'
            datetime_0 = date_time_format_0.validate(str_0)
            str_1 = '2023-03-15T14:30:45+02:00'
            datetime_1 = date_time_format_0.validate(str_1)
            int_0 = 2
            timedelta_0 = module_2.timedelta()
            str_2 = '2023-03-15T14:30:45'
            datetime_2 = date_time_format_0.validate(str_2)
            str_3 = '2023-15-03T14:30:45'
            datetime_3 = date_time_format_0.validate(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
