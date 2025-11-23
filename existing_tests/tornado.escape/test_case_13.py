import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'f0{lK{"7|'
            str_1 = module_0.xhtml_escape(str_0)
            bool_0 = True
            optional_0 = module_0.utf8(str_0)
            list_0 = [str_0]
            any_0 = module_0.recursive_unicode(str_0)
            any_1 = module_0.recursive_unicode(list_0)
            str_2 = module_0.xhtml_unescape(str_0)
            any_2 = module_0.recursive_unicode(str_1)
            str_3 = module_0.linkify(str_0, str_2, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
