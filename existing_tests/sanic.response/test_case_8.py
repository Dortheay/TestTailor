import unittest
import timeout_decorator
import sanic.response as module_0

class Test_Response_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'X(=Txm'
        h_t_t_p_response_0 = module_0.html(str_0)
        list_0 = [h_t_t_p_response_0, str_0, str_0]
        streaming_h_t_t_p_response_0 = module_0.StreamingHTTPResponse(list_0)

if __name__ == "__main__":
    unittest.main()
