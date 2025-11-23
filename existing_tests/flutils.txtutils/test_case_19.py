import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        int_0 = 112
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
        str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and (%r)."
        str_1 = ansi_text_wrapper_0.fill(str_0)
        int_1 = -2713
        str_2 = ''
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, int_1, max_lines=int_1, placeholder=str_0)
        list_0 = ansi_text_wrapper_0.wrap(str_2)

if __name__ == "__main__":
    unittest.main()
