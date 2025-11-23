import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '4_x^*A=<>dTR:l4jDE["'
        str_1 = module_0.json_encode(str_0)
        str_2 = module_0.squeeze(str_1)
        bool_0 = True
        str_3 = module_0.xhtml_escape(str_0)
        bool_1 = True
        optional_0 = module_0.utf8(str_2)
        any_0 = module_0.recursive_unicode(str_0)
        any_1 = module_0.recursive_unicode(bool_1)
        var_0 = module_0.url_unescape(str_3, bool_0)
        optional_1 = module_0.to_unicode(str_3)
        str_4 = "i#<SJ,`6Q8Fg'9)g&T|9"
        str_5 = module_0.xhtml_escape(str_4)
        str_6 = module_0.linkify(str_5, str_5)
        bytes_0 = b'&[c;\xdd'
        dict_0 = module_0.parse_qs_bytes(str_5)
        optional_2 = module_0.to_unicode(str_4)
        str_7 = module_0.xhtml_unescape(str_5)
        optional_3 = module_0.utf8(bytes_0)

if __name__ == "__main__":
    unittest.main()
