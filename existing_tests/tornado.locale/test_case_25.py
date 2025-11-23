import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            str_0 = None
            module_0.load_gettext_translations(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
