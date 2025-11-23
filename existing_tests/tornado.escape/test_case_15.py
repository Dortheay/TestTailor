import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = 'f0{lK{"7|'
            bool_0 = True
            bool_1 = True
            optional_0 = module_0.utf8(str_0)
            list_0 = []
            any_0 = module_0.recursive_unicode(bool_0)
            any_1 = module_0.recursive_unicode(bool_1)
            str_1 = module_0.linkify(str_0, bool_1, str_0, list_0)
            optional_1 = module_0.to_unicode(str_1)
            var_0 = module_0.url_unescape(str_0, bool_0)
            optional_2 = module_0.to_unicode(str_0)
            str_2 = "i#<SJ,`6Q8Fg'9)g&T|9"
            str_3 = module_0.squeeze(str_0)
            str_4 = module_0.xhtml_escape(str_2)
            str_5 = module_0.linkify(str_4, str_4)
            str_6 = '2(\x0c(%\r'
            bytes_0 = b'\xb1i\x90\x83\xe5_\xa5\xb3\x13\r\xba\x8e\xac\x19'
            bool_2 = None
            var_1 = module_0.url_unescape(str_6, bool_2)
            any_2 = module_0.recursive_unicode(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
