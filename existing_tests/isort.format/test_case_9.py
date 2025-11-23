import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = ' unable to sort due to existing syntax errors'
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_0.diff_line(str_0)

if __name__ == "__main__":
    unittest.main()
