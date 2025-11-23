import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1
import typing as module_2

class Test_Format_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = ' but was given a literal of type '
            str_1 = 'U\x0c>5Ql4eJ\x0b2!Er%C\t,\\,'
            colorama_printer_0 = module_0.ColoramaPrinter()
            basic_printer_0 = module_0.BasicPrinter()
            basic_printer_0.error(str_1)
            basic_printer_1 = module_0.BasicPrinter()
            basic_printer_1.success(str_0)
            str_2 = '|3q3=^t'
            str_3 = 'S{'
            basic_printer_1.error(str_3)
            str_4 = module_0.format_natural(str_2)
            basic_printer_2 = module_0.BasicPrinter()
            str_5 = '>+dxO*p!#Gco-'
            basic_printer_2.error(str_5)
            str_6 = None
            str_7 = '|g\r\\ !{G'
            str_8 = module_0.format_simplified(str_7)
            none_type_0 = None
            var_0 = module_0.show_unified_diff(file_input=str_6, file_output=str_4, file_path=none_type_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
