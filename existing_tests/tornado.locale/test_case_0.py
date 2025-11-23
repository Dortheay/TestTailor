import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'Tampered cookie %r'
        module_0.set_default_locale(str_0)

if __name__ == "__main__":
    unittest.main()
