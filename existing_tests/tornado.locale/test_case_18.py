import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '<{0} [{1}]>'
            list_0 = [str_0]
            locale_0 = module_0.get()
            str_1 = locale_0.list(list_0)
            locale_1 = module_0.Locale(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
