import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            time_format_0 = module_0.TimeFormat()
            str_0 = '2023-03-32T14:30:45'
            list_0 = []
            date_time_format_0 = module_0.DateTimeFormat(*list_0)
            datetime_0 = date_time_format_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
