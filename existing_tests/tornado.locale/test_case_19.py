import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '.?k%\n/caH5'
            iterable_0 = module_0.get_supported_locales()
            null_translations_0 = module_1.NullTranslations()
            str_1 = '^}$q2f.h)aN(d`NW#'
            list_0 = [str_0, str_1]
            locale_0 = module_0.get(*list_0)
            int_0 = -1692
            str_2 = locale_0.friendly_number(int_0)
            module_0.load_translations(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
