import unittest
import timeout_decorator
import tornado.locale as module_0
import gettext as module_1

class Test_Locale_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = None
            str_1 = '"EX\rlnzc >_=MRa*'
            list_0 = [str_1]
            locale_0 = module_0.get(*list_0)
            str_2 = locale_0.translate(str_0, str_0)
            locale_1 = module_0.get(*list_0)
            locale_2 = module_0.get(*list_0)
            module_0.load_translations(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
