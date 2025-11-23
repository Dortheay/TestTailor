import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'm1d_M-:MR^X#'
            locale_0 = module_0.Locale(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
