import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = 7
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
        str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and (%r)."
        str_1 = ansi_text_wrapper_0.fill(str_0)
        str_2 = ansi_text_wrapper_0.fill(str_1)
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0)
        int_1 = -1125
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_0, max_lines=int_1)
        str_3 = 'Y5,npO4i\t<'
        str_4 = '\x0b'
        list_0 = ansi_text_wrapper_0.wrap(str_4)
        str_5 = ansi_text_wrapper_2.fill(str_3)

if __name__ == "__main__":
    unittest.main()
