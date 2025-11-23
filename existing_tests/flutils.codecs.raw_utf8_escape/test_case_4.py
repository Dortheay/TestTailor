import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'h\xf7\xb2\x10\xea\x06\x8bc\xf6'
            user_string_0 = module_0.UserString(bytes_0)
            str_0 = 'YUgXCX[k8%XL'
            tuple_0 = module_1.encode(user_string_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
