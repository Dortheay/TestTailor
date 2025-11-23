import unittest
import timeout_decorator
import collections as module_0
import flutils.codecs.raw_utf8_escape as module_1
import codecs as module_2

class Test_Raw_utf8_escape_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = False
            list_0 = [bool_0]
            dict_0 = {bool_0: bool_0, bool_0: list_0, bool_0: list_0}
            user_string_0 = module_0.UserString(dict_0)
            tuple_0 = module_1.encode(user_string_0, user_string_0)
            str_0 = ':lXs2M]D2zz;>V'
            tuple_1 = module_1.decode(bool_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
