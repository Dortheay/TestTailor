import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            time_format_0 = module_0.TimeFormat()
            str_0 = '14:30:15'
            time_0 = time_format_0.validate(str_0)
            str_1 = '14:30:15.123456'
            time_1 = time_format_0.validate(str_1)
            str_2 = 'invalid-time'
            time_2 = time_format_0.validate(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
