import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = '+L?u'
            str_1 = 'h4wA?/e!,2uH.%2'
            str_2 = 'Defines an option in the global namespace.\n\n    See `OptionParser.define`.\n    '
            dict_0 = {str_0: str_2}
            str_3 = ':N%2{TtBX/L\r\t'
            dict_1 = {str_0: dict_0, str_2: dict_0, str_3: dict_0}
            c_s_v_locale_0 = module_0.CSVLocale(str_0, dict_1)
            str_4 = c_s_v_locale_0.pgettext(str_1, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
