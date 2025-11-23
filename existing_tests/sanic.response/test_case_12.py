import unittest
import timeout_decorator
import sanic.response as module_0

class Test_Response_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        bytes_0 = b'\xc7\xd19<\xb8\x94\x85\x8a\x94\xb9\x87T\x91\xdd&$N'
        str_0 = '?,'
        str_1 = None
        dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0}
        base_h_t_t_p_response_0 = module_0.BaseHTTPResponse()
        base_h_t_t_p_response_0.send()
        h_t_t_p_response_0 = module_0.html(bytes_0, dict_0)

if __name__ == "__main__":
    unittest.main()
