import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = None
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            request_timeout_0 = module_0.RequestTimeout(str_0, dict_0)
            py_file_error_0 = module_0.PyFileError(request_timeout_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
