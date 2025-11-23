import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'bx'
            locale_0 = module_0.get()
            str_1 = locale_0.list(str_0)
            str_2 = '.?k%\n/caH5'
            module_0.load_translations(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
