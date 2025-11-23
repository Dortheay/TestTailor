import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 7
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, max_lines=int_0)
        str_0 = "The given value for 'position', %r, must be an 'int' between (%r) and (%r)."
        str_1 = ansi_text_wrapper_0.fill(str_0)
        bool_0 = False
        bool_1 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_0, bool_0, bool_1, bool_1, bool_1, int_0)
        int_1 = -1125
        bool_2 = None
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(int_1, bool_0, bool_2, bool_1)

if __name__ == "__main__":
    unittest.main()
