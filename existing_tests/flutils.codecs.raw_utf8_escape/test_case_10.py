import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'?/\x15:\n'
            user_string_0 = module_0.UserString(bytes_0)
            tuple_0 = module_1.encode(user_string_0, user_string_0)
            bytes_1 = b'\xcb\x14\xeb3u\tL\x89\xbd\xbc\x97\xbeK\xc4\x08\x1b\xd46<\xd6'
            str_0 = '\t"5<1'
            tuple_1 = module_1.decode(bytes_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
