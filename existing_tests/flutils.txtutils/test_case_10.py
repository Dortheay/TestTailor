import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 7
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
            str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and(%r)o"
            int_1 = 529
            str_1 = 'The name of the cherry-picking module attribute.'
            str_2 = ansi_text_wrapper_0.fill(str_1)
            bool_0 = True
            ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_1, str_0, bool_0, bool_0, bool_0)
            str_3 = ansi_text_wrapper_0.fill(str_0)
            str_4 = None
            str_5 = ansi_text_wrapper_0.fill(str_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
