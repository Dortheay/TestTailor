import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '/J2ZSKFb!~ed\rB?,:o'
            bool_0 = False
            bool_1 = True
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_1, bool_1)
            list_0 = ansi_text_wrapper_0.wrap(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
