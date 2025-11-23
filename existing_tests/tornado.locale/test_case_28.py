import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = '.Pk%\n\naHx'
            iterable_0 = module_0.get_supported_locales()
            null_translations_0 = module_1.NullTranslations()
            locale_0 = module_0.get()
            str_1 = '^}$q2f.h)aN(d`NW#'
            int_0 = -27
            list_0 = [str_0, str_1]
            locale_1 = module_0.get(*list_0)
            str_2 = locale_1.friendly_number(int_0)
            int_1 = -1692
            str_3 = locale_1.friendly_number(int_1)
            str_4 = locale_1.translate(str_1)
            datetime_0 = None
            bool_0 = locale_1.format_day(datetime_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
