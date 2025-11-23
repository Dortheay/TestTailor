import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            date_time_format_0 = module_0.DateTimeFormat()
            datetime_0 = date_time_format_0.validate(date_time_format_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
