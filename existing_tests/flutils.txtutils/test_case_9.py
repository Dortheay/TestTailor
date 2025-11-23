import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = 7
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
            str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and (%r)."
            str_1 = ansi_text_wrapper_0.fill(str_0)
            str_2 = ansi_text_wrapper_0.fill(str_0)
            bool_0 = True
            ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, str_0, str_0, bool_0)
            str_3 = 'v/kxGDY^H'
            bool_1 = False
            ansi_text_wrapper_2 = module_0.AnsiTextWrapper(str_3, bool_1, bool_1)
            str_4 = "2Z'{X8\\\x0c+ho)%uZh\x0c"
            list_0 = ansi_text_wrapper_1.wrap(str_4)
            str_5 = ansi_text_wrapper_2.fill(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
