import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = "xJH\rTg'Zybs:\\t_6w"
            int_0 = 1640
            str_1 = None
            list_0 = [str_1]
            locale_0 = module_0.get(*list_0)
            str_2 = locale_0.translate(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
