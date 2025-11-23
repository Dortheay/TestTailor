import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '.\rF3(lc[NO/m'
            list_0 = []
            date_time_format_0 = module_0.DateTimeFormat()
            bool_0 = date_time_format_0.is_native_type(str_0)
            date_time_format_1 = module_0.DateTimeFormat()
            date_time_format_2 = module_0.DateTimeFormat(*list_0)
            datetime_0 = date_time_format_2.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
