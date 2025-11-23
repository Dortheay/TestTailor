import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = 'unsupported compression parameter %r'
            str_1 = 'pvFYW\x0bCc^r\tmJ\x0besM$d1'
            str_2 = 'Ya|\x0cs\\F<htg*\\b'
            str_3 = 'ZHA'
            str_4 = '3{,W'
            optional_0 = None
            null_translations_0 = module_1.NullTranslations()
            gettext_locale_0 = module_0.GettextLocale(str_2, null_translations_0)
            str_5 = gettext_locale_0.pgettext(str_4, str_0, optional_0)
            int_0 = None
            locale_0 = module_0.get()
            str_6 = 's1lU'
            str_7 = locale_0.translate(str_6)
            null_translations_1 = module_1.NullTranslations()
            gettext_locale_1 = module_0.GettextLocale(str_2, null_translations_1)
            str_8 = gettext_locale_1.translate(str_3)
            str_9 = locale_0.list(str_1)
            bool_0 = True
            str_10 = locale_0.format_date(int_0, bool_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
