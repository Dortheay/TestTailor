import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'CefhS'
            int_0 = 1904
            null_translations_0 = module_1.NullTranslations()
            gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
            str_1 = gettext_locale_0.pgettext(str_0, str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
