import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'fcK'
        bool_0 = False
        bool_1 = None
        str_1 = module_0.linkify(str_0, bool_0, str_0, bool_1)
        str_2 = module_0.json_encode(str_1)
        any_0 = None
        str_3 = module_0.json_encode(any_0)
        optional_0 = module_0.to_unicode(str_3)
        str_4 = module_0.xhtml_escape(str_3)

if __name__ == "__main__":
    unittest.main()
