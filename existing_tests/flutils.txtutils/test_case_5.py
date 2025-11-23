import unittest
import timeout_decorator
import flutils.txtutils as module_0

class Test_Txtutils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 150
            str_0 = 'Pbp,xZ))d'
            int_1 = 1859
            ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_1, max_lines=int_0)
            str_1 = ansi_text_wrapper_0.fill(str_0)
            str_2 = 'normalize_path'
            int_2 = -441
            bool_0 = True
            str_3 = 'm6c+uWX/]nIC}?BU'
            ansi_text_wrapper_1 = module_0.AnsiTextWrapper(int_2, bool_0, bool_0, placeholder=str_3)
            list_0 = ansi_text_wrapper_0.wrap(str_2)
            list_1 = ansi_text_wrapper_0.wrap(str_0)
            bool_1 = True
            str_4 = '|PX3gAo [lD'
            ansi_text_wrapper_2 = module_0.AnsiTextWrapper(bool_1, max_lines=int_0, placeholder=str_4)
            str_5 = ansi_text_wrapper_2.fill(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
