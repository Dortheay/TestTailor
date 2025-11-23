import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = '4_x^*A=<>dTR:l4jDE["'
            str_1 = module_0.json_encode(str_0)
            str_2 = 'f0{lK{"7|'
            str_3 = module_0.squeeze(str_2)
            str_4 = module_0.xhtml_escape(str_2)
            optional_0 = module_0.utf8(str_2)
            list_0 = []
            any_0 = module_0.recursive_unicode(str_0)
            str_5 = "'a3XtD"
            tuple_0 = (str_5, str_2)
            any_1 = module_0.recursive_unicode(tuple_0)
            str_6 = module_0.linkify(str_4)
            optional_1 = module_0.to_unicode(str_2)
            var_0 = module_0.url_unescape(str_0)
            optional_2 = module_0.to_unicode(str_1)
            str_7 = "i#<SJ,`6Q8Fg'9)g&T|9"
            var_1 = module_0.url_unescape(str_0, str_4)
            str_8 = module_0.xhtml_unescape(str_5)
            str_9 = module_0.xhtml_escape(str_7)
            str_10 = module_0.linkify(str_9, list_0)
            bytes_0 = b'5/\xab\xb6\xd3\x1e\xe5\x9e\x13\xee\xcd\xaded'
            str_11 = module_0.squeeze(str_10)
            optional_3 = module_0.to_unicode(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
