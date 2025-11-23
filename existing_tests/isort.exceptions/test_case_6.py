import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '<Z2rKST[|cto\t^Uy!^6'
        exception_0 = module_1.Exception()
        literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_0, exception_0)

if __name__ == "__main__":
    unittest.main()
