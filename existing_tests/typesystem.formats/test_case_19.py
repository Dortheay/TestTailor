import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            time_format_0 = None
            date_format_0 = module_0.DateFormat()
            optional_0 = date_format_0.serialize(time_format_0)
            list_0 = [optional_0, time_format_0, date_format_0, date_format_0]
            date_time_format_0 = module_0.DateTimeFormat(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
