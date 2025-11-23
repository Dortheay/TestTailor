import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1
import typing as module_2

class Test_Format_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'from os import path'
            str_1 = module_0.format_natural(str_0)
            str_2 = 'import sys'
            str_3 = module_0.format_natural(str_2)
            str_4 = module_0.format_natural(str_2)
            str_5 = module_0.format_natural(str_2)
            basic_printer_0 = module_0.BasicPrinter()
            text_i_o_0 = module_2.TextIO()
            colorama_printer_0 = module_0.ColoramaPrinter(text_i_o_0)
            str_6 = colorama_printer_0.style_text(str_2, str_3)
            colorama_printer_1 = module_0.ColoramaPrinter(text_i_o_0)
            str_7 = module_0.format_simplified(str_5)
            str_8 = 'HSQIc9(;}TLCv(&gx9'
            bool_0 = False
            var_0 = module_0.create_terminal_printer(bool_0)
            basic_printer_0.success(str_8)
            str_9 = 'from-type place_module for '
            bool_1 = module_0.ask_whether_to_apply_changes_to_file(str_9)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
