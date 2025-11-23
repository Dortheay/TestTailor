import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        text_i_o_0 = None
        basic_printer_0 = module_0.BasicPrinter(text_i_o_0)
        colorama_printer_0 = module_0.ColoramaPrinter(basic_printer_0)
        str_0 = '?.*wmg-*434/o|'
        basic_printer_1 = module_0.BasicPrinter()
        basic_printer_1.diff_line(str_0)

if __name__ == "__main__":
    unittest.main()
