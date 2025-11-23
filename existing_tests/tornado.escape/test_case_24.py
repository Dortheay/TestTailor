import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '4_x^*A=<>dTR:l4jDE["'
        str_1 = module_0.json_encode(str_0)
        str_2 = 'f0{lK{"7|'
        str_3 = module_0.xhtml_escape(str_2)
        optional_0 = module_0.utf8(str_2)
        any_0 = module_0.recursive_unicode(str_0)
        str_4 = "i#<SJ,`6Q8Fg'9)g&T|9"
        str_5 = module_0.xhtml_unescape(str_3)
        str_6 = module_0.xhtml_escape(str_4)
        str_7 = module_0.linkify(str_6, str_6)
        str_8 = 'A'
        str_9 = module_0.squeeze(str_8)
        str_10 = '2(\x0c(%\r'
        dict_0 = module_0.parse_qs_bytes(str_10)
        str_11 = module_0.json_encode(str_7)
        str_12 = module_0.url_escape(str_4)
        bool_0 = True
        dict_1 = module_0.parse_qs_bytes(str_11, bool_0)

if __name__ == "__main__":
    unittest.main()
