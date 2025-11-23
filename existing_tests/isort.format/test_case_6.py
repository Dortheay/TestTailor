import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '&Z0][h&dB!x>2F^V4$'
        basic_printer_0 = module_0.BasicPrinter()
        basic_printer_0.error(str_0)

if __name__ == "__main__":
    unittest.main()
