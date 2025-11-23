import unittest
import timeout_decorator
import isort.exceptions as module_0
import builtins as module_1
import pathlib as module_2

class Test_Exceptions_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = '|}Y>E'
        dict_0 = {str_0: str_0}
        path_0 = module_2.Path(**dict_0)
        unsupported_encoding_0 = module_0.UnsupportedEncoding(path_0)
        str_1 = 'CB5N1q(k+0w'
        existing_syntax_errors_0 = module_0.ExistingSyntaxErrors(str_1)
        exception_0 = None
        literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_0, exception_0)
        file_skipped_0 = module_0.FileSkipped(str_1, str_1)

if __name__ == "__main__":
    unittest.main()
