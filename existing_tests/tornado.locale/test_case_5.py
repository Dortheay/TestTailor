import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'yn2'
        str_1 = 'a'
        null_translations_0 = module_1.NullTranslations()
        gettext_locale_0 = module_0.GettextLocale(str_1, null_translations_0)
        str_2 = gettext_locale_0.pgettext(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
