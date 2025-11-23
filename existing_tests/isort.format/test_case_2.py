import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = "~>1'X]kA~'Dt&tmVpA(L"
        str_1 = module_0.format_natural(str_0)
        basic_printer_0 = module_0.BasicPrinter()

if __name__ == "__main__":
    unittest.main()
