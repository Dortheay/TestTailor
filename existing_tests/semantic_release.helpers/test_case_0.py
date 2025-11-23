import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            session_0 = module_0.build_requests_session(bool_0, bool_0)
            int_0 = 0
            str_0 = 'response'
            var_0 = session_0.hooks[str_0][int_0]
            var_1 = callable(var_0)
            str_1 = 'http://'
            var_2 = session_0.adapters[str_1]
            str_2 = 'https://'
            var_3 = session_0.adapters[str_2]
            var_4 = session_0.adapters[str_1]
            var_5 = var_4.max_retries
            bool_1 = False
            session_1 = module_0.build_requests_session(bool_1, bool_0)
            int_1 = 5
            session_2 = module_0.build_requests_session(bool_0, int_1)
            var_6 = session_2.adapters[str_1]
            var_7 = var_6.max_retries
            int_2 = 3
            float_0 = 0.5
            retry_0 = module_1.Retry(int_2, float_0)
            session_3 = module_0.build_requests_session(bool_0, retry_0)
            var_8 = session_3.adapters[str_1]
            var_9 = var_8.max_retries
            bool_2 = True
            str_3 = 'invalid'
            session_4 = module_0.build_requests_session(bool_2, str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
