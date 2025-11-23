import unittest
import timeout_decorator
import isort.format as module_0
import pathlib as module_1

class Test_Format_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'fF(!!y:.soaJ\n~'
        str_1 = module_0.format_simplified(str_0)

if __name__ == "__main__":
    unittest.main()
