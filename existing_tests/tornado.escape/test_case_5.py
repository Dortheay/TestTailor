import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'iB`_HWv5&?~VQfo7q\\$#'
            bytes_0 = b'<%\xac\xb2\x04r\x98\x84\xa8\r\x83\xf6'
            list_0 = [bytes_0, bytes_0]
            list_1 = []
            dict_0 = {str_0: list_0, str_0: list_0, str_0: list_1}
            optional_0 = module_0.utf8(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
