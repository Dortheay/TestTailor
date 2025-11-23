import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '.Pk%\n\naHx'
        iterable_0 = module_0.get_supported_locales()
        bool_0 = True
        null_translations_0 = module_1.NullTranslations()
        str_1 = '^}$q2f.h)aN(d`NW#'
        list_0 = [str_0, str_1]
        locale_0 = module_0.get(*list_0)
        int_0 = -1692
        str_2 = locale_0.friendly_number(int_0)
        str_3 = locale_0.translate(str_1)
        str_4 = 'Deletes all the cookies the user sent with this request.\n\n        See `clear_cookie` for more information on the path and domain\n        parameters.\n\n        Similar to `set_cookie`, the effect of this method will not be\n        seen until the following request.\n\n        .. versionchanged:: 3.2\n\n           Added the ``path`` and ``domain`` parameters.\n        '
        str_5 = 'x{m"wZB]'
        str_6 = locale_0.pgettext(str_4, str_5)
        null_translations_1 = module_1.NullTranslations(bool_0)
        gettext_locale_0 = module_0.GettextLocale(str_3, null_translations_1)
        str_7 = '9QdH'
        str_8 = locale_0.translate(str_7)
        str_9 = gettext_locale_0.pgettext(str_0, str_2)
        str_10 = locale_0.list(list_0)
        bool_1 = True
        str_11 = locale_0.format_date(int_0, bool_0, bool_1, bool_1)

if __name__ == "__main__":
    unittest.main()
