import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = '.?k%\n/caH5'
            str_1 = 'x\\I^L'
            bool_0 = False
            null_translations_0 = module_1.NullTranslations(bool_0)
            gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
            str_2 = gettext_locale_0.pgettext(str_0, str_0)
            int_0 = -554
            str_3 = gettext_locale_0.translate(str_0, str_1, int_0)
            str_4 = None
            str_5 = gettext_locale_0.pgettext(str_0, str_2)
            module_0.load_translations(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
