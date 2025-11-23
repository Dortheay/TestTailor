import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '3v<-'
        str_1 = 'uv[_Z?@!\x0cbz]!tpH'
        str_2 = '0K{p'
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_0.diff_line(str_2)
        str_3 = 'hA4l*JX@q'
        path_0 = module_1.Path()
        var_0 = module_0.show_unified_diff(file_input=str_1, file_output=str_3, file_path=path_0)
        bytes_0 = b'f^\xeb\x0bHi\xfc\xbf\xdcu\\a'
        str_4 = '.Please see the 5.0.0 upgrade guide: bit.ly/isortv5.'
        colorama_printer_0.diff_line(str_4)
        basic_printer_0 = module_0.BasicPrinter(bytes_0)
        basic_printer_0.error(str_0)
        basic_printer_0.error(str_4)

if __name__ == "__main__":
    unittest.main()
