import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '"t.zjm?Tv'
            base_format_0 = module_0.BaseFormat()
            bool_0 = base_format_0.is_native_type(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
