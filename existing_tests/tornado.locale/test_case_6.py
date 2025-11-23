import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'xeI^b'
        bool_0 = False
        null_translations_0 = module_1.NullTranslations()
        locale_0 = module_0.get()
        str_1 = locale_0.translate(str_0)
        null_translations_1 = module_1.NullTranslations(bool_0)
        str_2 = 'x,O}i|&Hqq?^g;U*OS'
        list_0 = [str_2]
        locale_1 = module_0.get(*list_0)
        str_3 = ''
        str_4 = locale_1.list(str_3)
        int_0 = 445
        bool_1 = True
        str_5 = locale_0.format_date(int_0, bool_1)
        str_6 = locale_1.list(str_1)
        str_7 = locale_0.format_date(int_0)

if __name__ == "__main__":
    unittest.main()
