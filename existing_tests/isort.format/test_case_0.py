import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        basic_printer_0 = module_0.BasicPrinter()

if __name__ == "__main__":
    unittest.main()
