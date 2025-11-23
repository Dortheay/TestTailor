import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '>fgu-'
            locale_0 = module_0.get()
            int_0 = 1496
            str_1 = locale_0.friendly_number(int_0)
            str_2 = locale_0.list(str_0)
            str_3 = '\\BR?f;{"<1i,K'
            str_4 = locale_0.translate(str_3, str_0, int_0)
            str_5 = 'jIsG\r1%-'
            str_6 = locale_0.translate(str_0)
            list_0 = []
            locale_1 = module_0.get(*list_0)
            str_7 = locale_1.translate(str_5)
            module_0.load_translations(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
