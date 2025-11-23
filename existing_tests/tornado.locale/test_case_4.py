import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        iterable_0 = module_0.get_supported_locales()
        str_0 = 'queu/ non-empty, ?hy are getters waiting'
        int_0 = -1116
        int_1 = 2016
        null_translations_0 = module_1.NullTranslations(int_1)
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
        str_1 = gettext_locale_0.pgettext(str_0, str_0, str_0, int_0)
        iterable_1 = module_0.get_supported_locales()

if __name__ == "__main__":
    unittest.main()
