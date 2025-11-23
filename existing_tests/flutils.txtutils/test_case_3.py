import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = False
            int_0 = None
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0, int_0, max_lines=int_0)
            str_0 = None
            str_1 = ansi_text_wrapper_0.fill(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
