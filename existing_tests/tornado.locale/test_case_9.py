import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = '.Pk%\n\naHx'
        iterable_0 = module_0.get_supported_locales()
        bool_0 = True
        null_translations_0 = module_1.NullTranslations()
        locale_0 = module_0.get()
        str_1 = '^}$q2f.h)aN(d`NW#'
        int_0 = 1
        list_0 = [str_0, str_1]
        str_2 = locale_0.translate(str_0, str_1, int_0)
        locale_1 = module_0.get(*list_0)
        str_3 = locale_1.friendly_number(int_0)
        int_1 = -1692
        str_4 = locale_1.friendly_number(int_1)
        str_5 = locale_1.translate(str_1)
        str_6 = 'x{m"wZB]'
        str_7 = locale_1.pgettext(str_0, str_6)
        gettext_locale_0 = module_0.GettextLocale(str_5, null_translations_0)
        str_8 = gettext_locale_0.pgettext(str_0, str_4)
        str_9 = locale_1.list(list_0)
        str_10 = locale_1.format_date(int_0, bool_0)
        gettext_locale_1 = module_0.GettextLocale(str_4, null_translations_0)
        null_translations_1 = module_1.NullTranslations()
        gettext_locale_2 = module_0.GettextLocale(str_7, null_translations_1)
        str_11 = '?zEFAP+.$h\x0b%s\\'
        str_12 = "'_xsrf' argument missing from POST"
        str_13 = '^'
        gettext_locale_3 = module_0.GettextLocale(str_13, null_translations_0)
        str_14 = 'Object representing a locale.\n\n    After calling one of `load_translations` or `load_gettext_translations`,\n    call `get` or `get_closest` to get a Locale object.\n    '
        str_15 = gettext_locale_0.pgettext(str_14, str_11, str_12, int_0)

if __name__ == "__main__":
    unittest.main()
