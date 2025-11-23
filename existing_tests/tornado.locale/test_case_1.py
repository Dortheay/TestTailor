import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        iterable_0 = module_0.get_supported_locales()
        float_0 = 1495.4468
        bool_0 = True
        locale_0 = module_0.get()
        str_0 = locale_0.format_date(float_0, bool_0)

if __name__ == "__main__":
    unittest.main()
