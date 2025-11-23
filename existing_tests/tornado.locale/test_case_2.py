import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'CefhS'
        str_1 = 'c,4}Cs\r*}Y8'
        str_2 = None
        str_3 = 'WX)T@PEJQ'
        list_0 = [str_2, str_2, str_3, str_2]
        locale_0 = module_0.get(*list_0)
        str_4 = locale_0.pgettext(str_0, str_1)

if __name__ == "__main__":
    unittest.main()
