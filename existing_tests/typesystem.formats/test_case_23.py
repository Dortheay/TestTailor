import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            date_time_format_0 = module_0.DateTimeFormat()
            int_0 = 12
            int_1 = 123456
            str_0 = '2023-03-15T14:30:45+02:00'
            datetime_0 = date_time_format_0.validate(str_0)
            timedelta_0 = module_2.timedelta()
            list_0 = [datetime_0, int_1, datetime_0]
            date_time_format_1 = module_0.DateTimeFormat(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
