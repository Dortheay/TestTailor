import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        bytes_0 = b''
        str_0 = module_0.xhtml_unescape(bytes_0)
        str_1 = '#'
        dict_0 = module_0.parse_qs_bytes(str_0)
        any_0 = module_0.recursive_unicode(str_0)
        bool_0 = False
        str_2 = module_0.url_escape(str_1, bool_0)
        optional_0 = module_0.to_unicode(bytes_0)
        any_1 = module_0.recursive_unicode(str_0)
        any_2 = module_0.recursive_unicode(dict_0)
        str_3 = None
        str_4 = module_0.json_encode(str_3)

if __name__ == "__main__":
    unittest.main()
