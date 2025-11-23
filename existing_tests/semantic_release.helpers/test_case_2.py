import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = None
        list_0 = [float_0, float_0, float_0, float_0]
        bytes_0 = b'\x8c\xf7\xfe'
        int_0 = 2520
        retry_0 = module_1.Retry(float_0, list_0, float_0, bytes_0, int_0)
        session_0 = module_0.build_requests_session(retry_0)
        var_0 = module_0.format_arg(session_0)

if __name__ == "__main__":
    unittest.main()
