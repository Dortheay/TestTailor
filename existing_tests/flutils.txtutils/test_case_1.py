import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'o'
            str_1 = '|`P mPK\x0c!=07S'
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(str_1)
            list_0 = ansi_text_wrapper_0.wrap(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
