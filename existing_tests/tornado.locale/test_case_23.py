import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'TV2'
            int_0 = -1074
            str_1 = 'p!@4UijaF\n8,'
            null_translations_0 = module_1.NullTranslations()
            gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
            str_2 = gettext_locale_0.translate(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
