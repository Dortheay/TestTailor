import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'K4]U'
            str_1 = module_0.linkify(str_0)
            str_2 = module_0.xhtml_unescape(str_1)
            bool_0 = None
            var_0 = module_0.url_unescape(str_1, str_1, bool_0)
            str_3 = module_0.json_encode(bool_0)
            optional_0 = module_0.utf8(str_2)
            bytes_0 = b'\xfe\xcb\xc2\xaa'
            bool_1 = True
            str_4 = module_0.url_escape(bytes_0, bool_1)
            str_5 = None
            str_6 = module_0.squeeze(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
