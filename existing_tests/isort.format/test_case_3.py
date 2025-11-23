import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'from os import path'
        str_1 = module_0.format_natural(str_0)
        str_2 = 'import sys'
        str_3 = module_0.format_natural(str_2)
        str_4 = 'os.path'
        str_5 = module_0.format_natural(str_4)

if __name__ == "__main__":
    unittest.main()
