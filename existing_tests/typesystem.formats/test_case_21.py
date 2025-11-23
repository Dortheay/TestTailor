import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            date_format_0 = module_0.DateFormat()
            str_0 = '2023-02-30'
            bool_0 = date_format_0.is_native_type(date_format_0)
            date_0 = date_format_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
