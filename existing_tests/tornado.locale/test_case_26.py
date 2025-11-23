import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = '.?k%\n/caH5'
            str_1 = 'x\\I^L'
            null_translations_0 = module_1.NullTranslations()
            gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)
            str_2 = "f^0j'f\x0bJ~/5Qo<&"
            locale_0 = module_0.get()
            str_3 = 'static_hash_cache'
            gettext_locale_1 = module_0.GettextLocale(str_3, null_translations_0)
            str_4 = gettext_locale_0.pgettext(str_1, str_3)
            int_0 = None
            str_5 = 'Uoi=(!{.<E\\+or[prk'
            list_0 = [str_5, str_5, str_4]
            locale_1 = module_0.get(*list_0)
            str_6 = locale_0.translate(str_3, int_0)
            dict_0 = {}
            null_translations_1 = module_1.NullTranslations(dict_0)
            str_7 = '"d{)miUUxCVg'
            gettext_locale_2 = module_0.GettextLocale(str_7, null_translations_0)
            str_8 = gettext_locale_1.translate(str_4, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
