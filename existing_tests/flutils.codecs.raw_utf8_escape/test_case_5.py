import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            module_1.register()
            module_1.register()
            module_1.register()
            bytes_0 = b'\xd3t\xb6,7\xe7\xc30\x1f\xb0pI'
            int_0 = 2037
            module_1.register()
            tuple_0 = (bytes_0, int_0)
            user_string_0 = module_0.UserString(tuple_0)
            tuple_1 = module_1.encode(user_string_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
