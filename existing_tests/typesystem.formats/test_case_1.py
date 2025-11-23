import unittest
import timeout_decorator
import typesystem.formats as module_0

class Test_Formats_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\xf9!/6&\xd7\xb3XY\xd0\x0f\x18T\xed\x96\x87F'
        date_format_0 = module_0.DateFormat()
        bool_0 = date_format_0.is_native_type(bytes_0)

if __name__ == "__main__":
    unittest.main()
