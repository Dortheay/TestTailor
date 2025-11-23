import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        complex_0 = None
        dict_0 = {complex_0: complex_0, complex_0: complex_0}
        list_0 = [dict_0, dict_0]
        header_not_found_0 = None
        request_timeout_0 = module_0.RequestTimeout(dict_0)
        payload_too_large_0 = module_0.PayloadTooLarge(request_timeout_0)
        sanic_exception_0 = module_0.SanicException(payload_too_large_0)
        not_found_0 = module_0.NotFound(header_not_found_0, request_timeout_0, sanic_exception_0)
        bytes_0 = b'V -\xfa6\r'
        header_expectation_failed_0 = module_0.HeaderExpectationFailed(bytes_0, list_0)
        forbidden_0 = module_0.Forbidden(header_expectation_failed_0)
        request_timeout_1 = module_0.RequestTimeout(not_found_0, forbidden_0)
        server_error_0 = module_0.ServerError(request_timeout_1)
        sanic_exception_1 = module_0.SanicException(list_0)
        not_found_1 = module_0.NotFound(complex_0, dict_0)

if __name__ == "__main__":
    unittest.main()
