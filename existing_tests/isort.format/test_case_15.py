import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1
import typing as module_2

class Test_Format_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 't,)t2_=v.-tfu\x0bV8:~'
            path_0 = module_1.Path()
            basic_printer_0 = module_0.BasicPrinter()
            bool_0 = False
            var_0 = module_0.create_terminal_printer(bool_0)
            basic_printer_0.error(str_0)
            str_1 = '||?k l'
            basic_printer_0.diff_line(str_1)
            basic_printer_1 = module_0.BasicPrinter(path_0)
            basic_printer_1.success(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
