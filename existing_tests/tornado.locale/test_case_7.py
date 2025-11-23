import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'x\\I^L'
        bool_0 = True
        null_translations_0 = module_1.NullTranslations()
        str_1 = "f^0j'f\x0bJ~/5Qo<&"
        list_0 = [str_0, str_1]
        locale_0 = module_0.get(*list_0)
        locale_1 = module_0.get()
        int_0 = -1692
        str_2 = locale_1.translate(str_1)
        null_translations_1 = module_1.NullTranslations(bool_0)
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_1)
        str_3 = gettext_locale_0.pgettext(str_2, str_2)
        str_4 = locale_1.translate(str_2, str_2, int_0)
        locale_2 = module_0.get()
        int_1 = 1532
        bool_1 = False
        str_5 = locale_0.format_date(int_0, int_1, bool_1)

if __name__ == "__main__":
    unittest.main()
