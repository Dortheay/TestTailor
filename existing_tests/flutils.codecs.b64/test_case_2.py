import unittest
import timeout_decorator
import flutils.codecs.b64 as module_0
import collections as module_1
import codecs as module_2

class Test_B64_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xd7\xd2\xfc\xefy\x86\x18`Wl\xc2\xf1'
            user_string_0 = module_1.UserString(bytes_0)
            tuple_0 = module_0.encode(user_string_0)
            str_0 = 'You do not have execute permission to run the file: %r'
            tuple_1 = module_0.encode(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
