import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '`7#:\x0bx$zi|VO$q}$I~xG'
        str_1 = module_0.json_encode(str_0)
        optional_0 = module_0.utf8(str_0)
        bool_0 = True
        var_0 = module_0.url_unescape(str_0, bool_0)
        list_0 = [str_0]
        str_2 = '`b'
        str_3 = module_0.squeeze(str_2)
        str_4 = module_0.linkify(str_1, list_0)
        any_0 = module_0.json_decode(str_1)
        str_5 = module_0.linkify(str_1)
        str_6 = module_0.linkify(str_5, bool_0)
        optional_1 = module_0.utf8(str_0)
        str_7 = module_0.url_escape(str_1)
        str_8 = 'v`?e`RAiu"f0I^-1'
        dict_0 = module_0.parse_qs_bytes(str_8, bool_0)
        dict_1 = module_0.parse_qs_bytes(str_2, bool_0)
        str_9 = module_0.linkify(str_1, list_0)
        str_10 = module_0.squeeze(str_5)

if __name__ == "__main__":
    unittest.main()
