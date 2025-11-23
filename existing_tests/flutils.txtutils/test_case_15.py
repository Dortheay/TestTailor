import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        int_0 = 7
        str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and (%r)."
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
        int_1 = -1125
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0, max_lines=int_1)
        str_1 = 'Y5,nJO4i\t<'
        str_2 = ansi_text_wrapper_1.fill(str_1)

if __name__ == "__main__":
    unittest.main()
