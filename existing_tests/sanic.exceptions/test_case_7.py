import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x10A\x81\xe7'
            py_file_error_0 = module_0.PyFileError(bytes_0)
            payload_too_large_0 = module_0.PayloadTooLarge(py_file_error_0)
            header_not_found_0 = module_0.HeaderNotFound(payload_too_large_0)
            str_0 = 'cqO]lu'
            str_1 = '07o:Z>x#*9h$jfip'
            str_2 = '0:"%Zz^c\ne@<[i0z'
            py_file_error_1 = module_0.PyFileError(str_2)
            dict_0 = {str_0: bytes_0, str_1: py_file_error_1, str_1: str_0, str_2: header_not_found_0}
            server_error_0 = module_0.ServerError(dict_0)
            str_3 = 'Unknown Expect: '
            request_timeout_0 = module_0.RequestTimeout(str_3)
            dict_1 = {request_timeout_0: payload_too_large_0}
            sanic_exception_0 = module_0.SanicException(dict_1)
            float_0 = 1520.599
            method_not_supported_0 = module_0.MethodNotSupported(header_not_found_0, dict_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
