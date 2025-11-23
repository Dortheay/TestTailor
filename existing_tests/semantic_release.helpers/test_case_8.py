import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        float_0 = -1500.176
        logged_function_0 = module_0.LoggedFunction(float_0)
        bool_0 = True
        dict_0 = None
        complex_0 = None
        bool_1 = False
        list_0 = [dict_0]
        bytes_0 = b'\xc2u4$E5,\xef\x17\xc1'
        dict_1 = {logged_function_0: float_0, dict_0: list_0, float_0: complex_0}
        retry_0 = module_1.Retry(list_0, bytes_0, bytes_0, list_0, dict_1, dict_0)
        session_0 = module_0.build_requests_session(dict_0)
        tuple_0 = (list_0,)
        retry_1 = module_1.Retry(logged_function_0, retry_0, session_0, dict_1, tuple_0)
        list_1 = [float_0]
        retry_2 = module_1.Retry(bool_1, retry_1, list_1, tuple_0, retry_1)
        retry_3 = module_1.Retry(logged_function_0, bool_0, dict_0, complex_0, retry_2)
        logged_function_1 = module_0.LoggedFunction(retry_3)
        str_0 = 'Tag '
        logged_function_2 = module_0.LoggedFunction(str_0)
        retry_4 = None
        session_1 = module_0.build_requests_session(logged_function_2, retry_4)

if __name__ == "__main__":
    unittest.main()
