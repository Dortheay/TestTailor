import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b':\x83eS=\xac'
        str_0 = '+[0r{c)q'
        list_0 = []
        file_not_found_0 = module_0.FileNotFound(bytes_0, str_0, list_0)
        int_0 = -557
        dict_0 = {str_0: list_0, str_0: bytes_0}
        unauthorized_0 = module_0.Unauthorized(int_0, **dict_0)

if __name__ == "__main__":
    unittest.main()
