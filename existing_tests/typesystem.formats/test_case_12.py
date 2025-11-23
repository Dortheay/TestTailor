import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            set_0 = None
            u_u_i_d_format_0 = module_0.UUIDFormat()
            bool_0 = u_u_i_d_format_0.is_native_type(set_0)
            date_time_format_0 = module_0.DateTimeFormat()
            optional_0 = date_time_format_0.serialize(set_0)
            str_0 = '.\rF3(lc[NO/m'
            list_0 = []
            date_time_format_1 = module_0.DateTimeFormat(*list_0)
            datetime_0 = date_time_format_1.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
