import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_24(self):
        try:
            date_time_format_0 = module_0.DateTimeFormat()
            str_0 = '2023-03-15T14:30:05'
            datetime_0 = date_time_format_0.validate(str_0)
            int_0 = 45
            optional_0 = date_time_format_0.serialize(datetime_0)
            optional_1 = date_time_format_0.serialize(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
