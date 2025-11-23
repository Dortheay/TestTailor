import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            int_0 = 3
            dict_0 = {}
            list_0 = [int_0, dict_0, int_0]
            time_format_0 = module_0.TimeFormat()
            tuple_0 = (list_0, time_format_0)
            u_u_i_d_format_0 = module_0.UUIDFormat()
            str_0 = u_u_i_d_format_0.serialize(tuple_0)
            date_format_0 = module_0.DateFormat(**dict_0)
            optional_0 = date_format_0.serialize(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
