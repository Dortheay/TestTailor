import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '[WQvNRd3XrnC:BHNifp'
            module_0.load_translations(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
