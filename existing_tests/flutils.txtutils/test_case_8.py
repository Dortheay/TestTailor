import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = 7
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
            str_0 = "The given value for 'position', %r,must be an 'int' between (%r) and (%r)."
            str_1 = ansi_text_wrapper_0.fill(str_0)
            str_2 = ''
            str_3 = ansi_text_wrapper_0.fill(str_2)
            str_4 = ansi_text_wrapper_0.fill(str_1)
            str_5 = None
            str_6 = 'm6c+uWX/]nIC}?BU'
            int_1 = 2744
            ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_1, str_6)
            list_0 = ansi_text_wrapper_1.wrap(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
