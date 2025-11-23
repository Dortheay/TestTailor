import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '^'
            tuple_0 = module_1.encode(str_0)
            bytes_0 = b'\xb3'
            tuple_1 = module_1.decode(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
