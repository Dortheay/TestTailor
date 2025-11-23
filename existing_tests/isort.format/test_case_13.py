import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1
import typing as module_2

class Test_Format_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'jUcBV5UZ6[@g\t$'
            colorama_printer_0 = module_0.ColoramaPrinter()
            colorama_printer_0.diff_line(str_0)
            str_1 = 'Tells isort to follow symlinks that are encountered when running recursively.'
            str_2 = module_0.remove_whitespace(str_1)
            str_3 = 'jEK N8D*k'
            list_0 = [str_3]
            path_0 = module_1.Path(*list_0)
            str_4 = module_0.remove_whitespace(str_3)
            bool_0 = False
            var_0 = module_0.show_unified_diff(file_input=str_3, file_output=str_3, file_path=path_0, color_output=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
