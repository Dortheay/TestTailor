import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1
import typing as module_2

class Test_Format_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'uv[_Z?@!\x0cbz]!tpH'
            str_1 = module_0.remove_whitespace(str_0)
            str_2 = '0MN|'
            colorama_printer_0 = module_0.ColoramaPrinter()
            str_3 = 'hA4l*JX@q'
            path_0 = module_1.Path()
            var_0 = module_0.show_unified_diff(file_input=str_1, file_output=str_3, file_path=path_0)
            str_4 = ' Imports are incorrectly sorted and/or formatted.'
            str_5 = module_0.format_natural(str_4)
            colorama_printer_0.diff_line(str_1)
            str_6 = colorama_printer_0.style_text(str_2, str_1)
            str_7 = 'KT14VXNZ\\h9'
            str_8 = module_0.format_simplified(str_7)
            basic_printer_0 = module_0.BasicPrinter()
            str_9 = '<s-e GH"rEQ@7AW\x0c8o'
            colorama_printer_1 = module_0.ColoramaPrinter()
            str_10 = colorama_printer_1.style_text(str_9)
            str_11 = module_0.format_simplified(str_5)
            str_12 = '\\^hHA'
            basic_printer_0.success(str_12)
            str_13 = '\n:@i*;Y/'
            bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_13)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
