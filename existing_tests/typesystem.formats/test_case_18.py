import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            set_0 = None
            date_time_format_0 = module_0.DateTimeFormat()
            optional_0 = date_time_format_0.serialize(set_0)
            str_0 = '.\rF3(lc[NO/m'
            list_0 = []
            time_format_0 = module_0.TimeFormat(*list_0)
            optional_1 = time_format_0.serialize(set_0)
            datetime_0 = date_time_format_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
