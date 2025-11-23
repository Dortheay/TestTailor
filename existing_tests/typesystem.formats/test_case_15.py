import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            bytes_0 = b'\xb7t{\xe0\xe7'
            list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
            base_format_0 = module_0.BaseFormat()
            optional_0 = base_format_0.serialize(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
