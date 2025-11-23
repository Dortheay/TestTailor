import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = 7
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_0)
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
        str_0 = 'Y5,nJO4i\t<'
        str_1 = ansi_text_wrapper_2.fill(str_0)

if __name__ == "__main__":
    unittest.main()
