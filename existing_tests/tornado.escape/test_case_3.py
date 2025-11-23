import unittest
import timeout_decorator
import tornado.escape as module_0

class Test_Escape_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = "l+/]\r<b]'."
            str_1 = module_0.xhtml_unescape(str_0)
            optional_0 = module_0.to_unicode(str_0)
            any_0 = module_0.recursive_unicode(str_0)
            str_2 = module_0.url_escape(str_0)
            str_3 = '$ttTi\rN)!S3JR'
            str_4 = module_0.squeeze(str_2)
            str_5 = module_0.xhtml_escape(str_1)
            var_0 = module_0.url_unescape(str_2)
            any_1 = module_0.json_decode(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
