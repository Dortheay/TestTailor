import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            locale_0 = module_0.get()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
