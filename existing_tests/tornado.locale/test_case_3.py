import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '>IklJ2(* F@7q'
        bool_0 = True
        null_translations_0 = module_1.NullTranslations(bool_0)
        gettext_locale_0 = module_0.GettextLocale(str_0, null_translations_0)

if __name__ == "__main__":
    unittest.main()
